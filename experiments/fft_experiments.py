"""Reproducible FFT experiments for the MATH307 final report.

The script compares a direct DFT, a recursive radix-2 FFT, and NumPy's FFT;
then applies frequency-domain filtering and compression to synthetic signals
and images.  All outputs are written to Report/generated.
"""

from __future__ import annotations

import csv
import math
import time
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Report" / "generated"
OUT.mkdir(parents=True, exist_ok=True)


def dft_direct(x: np.ndarray) -> np.ndarray:
    """Compute the DFT from its definition using a dense Vandermonde matrix."""
    x = np.asarray(x, dtype=np.complex128)
    n = x.size
    j = np.arange(n)
    k = j.reshape((n, 1))
    omega = np.exp(-2j * np.pi * k * j / n)
    return omega @ x


def fft_recursive(x: np.ndarray) -> np.ndarray:
    """Recursive Cooley-Tukey radix-2 FFT for power-of-two input lengths."""
    x = np.asarray(x, dtype=np.complex128)
    n = x.size
    if n == 1:
        return x.copy()
    if n % 2 != 0:
        raise ValueError("fft_recursive requires a power-of-two length")
    even = fft_recursive(x[::2])
    odd = fft_recursive(x[1::2])
    factor = np.exp(-2j * np.pi * np.arange(n) / n)
    return np.concatenate([even + factor[: n // 2] * odd, even + factor[n // 2 :] * odd])


def ifft_recursive(x: np.ndarray) -> np.ndarray:
    """Inverse transform implemented through the conjugate FFT identity."""
    x = np.asarray(x, dtype=np.complex128)
    return np.conjugate(fft_recursive(np.conjugate(x))) / x.size


def time_call(func, x: np.ndarray, repeats: int = 5) -> tuple[float, np.ndarray]:
    """Return the best runtime in seconds and the corresponding result."""
    best = math.inf
    result = None
    for _ in range(repeats):
        start = time.perf_counter()
        result = func(x)
        elapsed = time.perf_counter() - start
        best = min(best, elapsed)
    return best, result


def psnr(reference: np.ndarray, estimate: np.ndarray) -> float:
    mse = float(np.mean((reference.astype(float) - estimate.astype(float)) ** 2))
    if mse == 0:
        return math.inf
    return 20 * math.log10(255.0 / math.sqrt(mse))


def benchmark_fft() -> list[dict[str, float]]:
    rng = np.random.default_rng(307)
    rows = []
    sizes = [16, 32, 64, 128, 256, 512, 1024, 2048]
    for n in sizes:
        x = rng.normal(size=n) + 1j * rng.normal(size=n)
        dft_time = math.nan
        dft_err = math.nan
        if n <= 512:
            dft_time, dft_result = time_call(dft_direct, x, repeats=3)
            dft_err = float(np.linalg.norm(dft_result - np.fft.fft(x)) / np.linalg.norm(np.fft.fft(x)))
        fft_time, fft_result = time_call(fft_recursive, x, repeats=5)
        np_time, np_result = time_call(np.fft.fft, x, repeats=10)
        rows.append(
            {
                "N": n,
                "DFT_time_ms": dft_time * 1000 if not math.isnan(dft_time) else math.nan,
                "recursive_FFT_time_ms": fft_time * 1000,
                "numpy_FFT_time_ms": np_time * 1000,
                "DFT_relative_error": dft_err,
                "recursive_FFT_relative_error": float(np.linalg.norm(fft_result - np_result) / np.linalg.norm(np_result)),
            }
        )
    return rows


def signal_experiment() -> dict[str, float]:
    rng = np.random.default_rng(307)
    fs = 1024
    n = 1024
    t = np.arange(n) / fs
    clean = 1.15 * np.sin(2 * np.pi * 50 * t) + 0.65 * np.sin(2 * np.pi * 120 * t)
    noisy = clean + 0.35 * np.sin(2 * np.pi * 300 * t) + 0.32 * rng.normal(size=n)

    spectrum = np.fft.fft(noisy)
    freqs = np.fft.fftfreq(n, d=1 / fs)
    low_pass = np.abs(freqs) <= 160
    filtered = np.real(np.fft.ifft(spectrum * low_pass))

    clean_mse_noisy = float(np.mean((clean - noisy) ** 2))
    clean_mse_filtered = float(np.mean((clean - filtered) ** 2))
    improvement = 10 * math.log10(clean_mse_noisy / clean_mse_filtered)

    magnitudes = np.abs(spectrum[: n // 2])
    dominant = np.argsort(magnitudes)[-5:][::-1]
    dominant_freqs = [float(freqs[i]) for i in dominant]

    plt.figure(figsize=(8, 4))
    plt.plot(t[:250], clean[:250], label="Clean", linewidth=2)
    plt.plot(t[:250], noisy[:250], label="Noisy", alpha=0.45)
    plt.plot(t[:250], filtered[:250], label="Filtered", linewidth=1.8)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Signal denoising with FFT low-pass filtering")
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUT / "signal_filtering.png", dpi=180)
    plt.close()

    plt.figure(figsize=(8, 4))
    plt.stem(freqs[: n // 2], magnitudes, basefmt=" ", linefmt="C0-", markerfmt="C0o")
    plt.axvline(160, color="C3", linestyle="--", label="Low-pass cutoff")
    plt.xlim(0, 360)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.title("Frequency spectrum of noisy signal")
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUT / "signal_spectrum.png", dpi=180)
    plt.close()

    return {
        "noisy_mse": clean_mse_noisy,
        "filtered_mse": clean_mse_filtered,
        "snr_improvement_db": improvement,
        "dominant_frequencies_hz": dominant_freqs,
    }


def make_synthetic_image(size: int = 256) -> np.ndarray:
    image = Image.new("L", (size, size), color=42)
    draw = ImageDraw.Draw(image)
    for y in range(0, size, 16):
        shade = 80 + int(80 * y / size)
        draw.rectangle([0, y, size, y + 7], fill=shade)
    draw.rectangle([34, 40, 210, 92], outline=225, width=3)
    draw.ellipse([62, 108, 168, 214], outline=230, width=4)
    draw.line([20, 226, 235, 132], fill=210, width=3)
    draw.line([20, 132, 235, 226], fill=180, width=2)
    image = image.filter(ImageFilter.GaussianBlur(radius=0.4))
    return np.asarray(image, dtype=float)


def radial_mask(shape: tuple[int, int], radius: float, high_pass: bool = False) -> np.ndarray:
    rows, cols = shape
    y, x = np.ogrid[:rows, :cols]
    cy, cx = rows // 2, cols // 2
    dist = np.sqrt((y - cy) ** 2 + (x - cx) ** 2)
    mask = dist <= radius
    return ~mask if high_pass else mask


def image_experiment() -> dict[str, float]:
    rng = np.random.default_rng(307)
    clean = make_synthetic_image()
    noisy = np.clip(clean + rng.normal(0, 24, clean.shape), 0, 255)

    shifted = np.fft.fftshift(np.fft.fft2(noisy))
    low_mask = radial_mask(noisy.shape, radius=42)
    low_filtered = np.real(np.fft.ifft2(np.fft.ifftshift(shifted * low_mask)))
    low_filtered = np.clip(low_filtered, 0, 255)

    high_mask = radial_mask(noisy.shape, radius=22, high_pass=True)
    high_pass = np.log1p(np.abs(np.fft.ifft2(np.fft.ifftshift(shifted * high_mask))))
    high_pass = 255 * high_pass / np.max(high_pass)

    magnitude = np.log1p(np.abs(shifted))
    magnitude = 255 * magnitude / np.max(magnitude)

    thresholds = [0.50, 0.90, 0.95, 0.98, 0.99]
    compression_rows = []
    coeff = np.fft.fft2(clean)
    abs_coeff = np.abs(coeff).ravel()
    for keep_energy in thresholds:
        order = np.sort(abs_coeff**2)[::-1]
        cumulative = np.cumsum(order)
        cutoff_index = int(np.searchsorted(cumulative, keep_energy * cumulative[-1]))
        threshold = math.sqrt(order[cutoff_index])
        compressed_coeff = coeff * (np.abs(coeff) >= threshold)
        reconstruction = np.real(np.fft.ifft2(compressed_coeff))
        retained = int(np.count_nonzero(compressed_coeff))
        compression_rows.append(
            {
                "energy_retained": keep_energy,
                "coefficients_retained_percent": 100 * retained / coeff.size,
                "mse": float(np.mean((clean - reconstruction) ** 2)),
                "psnr_db": psnr(clean, reconstruction),
            }
        )

    denoise_metrics = {
        "noisy_psnr_db": psnr(clean, noisy),
        "low_pass_psnr_db": psnr(clean, low_filtered),
        "noisy_mse": float(np.mean((clean - noisy) ** 2)),
        "low_pass_mse": float(np.mean((clean - low_filtered) ** 2)),
        "low_pass_coefficients_percent": 100 * np.count_nonzero(low_mask) / low_mask.size,
    }

    fig, axes = plt.subplots(2, 3, figsize=(9, 6))
    panels = [
        (clean, "Clean synthetic image"),
        (noisy, "Noisy input"),
        (magnitude, "Log FFT magnitude"),
        (low_filtered, "Low-pass denoised"),
        (high_pass, "High-pass edges"),
        (np.abs(clean - low_filtered), "Absolute denoising error"),
    ]
    for ax, (arr, title) in zip(axes.ravel(), panels):
        ax.imshow(arr, cmap="gray", vmin=0, vmax=255)
        ax.set_title(title, fontsize=10)
        ax.axis("off")
    plt.tight_layout()
    plt.savefig(OUT / "image_fft_processing.png", dpi=180)
    plt.close()

    plt.figure(figsize=(7, 4))
    plt.plot(
        [row["coefficients_retained_percent"] for row in compression_rows],
        [row["psnr_db"] for row in compression_rows],
        marker="o",
    )
    plt.xlabel("Coefficients retained (%)")
    plt.ylabel("PSNR (dB)")
    plt.title("Frequency-domain image compression tradeoff")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUT / "compression_tradeoff.png", dpi=180)
    plt.close()

    with (OUT / "compression_results.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=compression_rows[0].keys())
        writer.writeheader()
        writer.writerows(compression_rows)

    return denoise_metrics | {"compression_rows": compression_rows}


def write_outputs(bench_rows: list[dict[str, float]], signal: dict[str, float], image: dict[str, float]) -> None:
    with (OUT / "benchmark_results.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=bench_rows[0].keys())
        writer.writeheader()
        writer.writerows(bench_rows)

    plt.figure(figsize=(7.5, 4.5))
    n = [row["N"] for row in bench_rows]
    dft = [row["DFT_time_ms"] for row in bench_rows]
    fft = [row["recursive_FFT_time_ms"] for row in bench_rows]
    npfft = [row["numpy_FFT_time_ms"] for row in bench_rows]
    plt.loglog(n[:6], dft[:6], marker="o", label="Direct DFT")
    plt.loglog(n, fft, marker="s", label="Recursive FFT")
    plt.loglog(n, npfft, marker="^", label="NumPy FFT")
    plt.xlabel("Signal length N")
    plt.ylabel("Best runtime (ms)")
    plt.title("Runtime comparison of DFT and FFT")
    plt.grid(True, which="both", alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUT / "runtime_comparison.png", dpi=180)
    plt.close()

    with (OUT / "summary_metrics.tex").open("w", encoding="utf-8") as f:
        f.write("% Auto-generated by experiments/fft_experiments.py\n")
        f.write(f"\\newcommand{{\\SignalNoisyMSE}}{{{signal['noisy_mse']:.4f}}}\n")
        f.write(f"\\newcommand{{\\SignalFilteredMSE}}{{{signal['filtered_mse']:.4f}}}\n")
        f.write(f"\\newcommand{{\\SignalImprovementDb}}{{{signal['snr_improvement_db']:.2f}}}\n")
        f.write(
            "\\newcommand{\\DominantFrequencies}{"
            + ", ".join(f"{freq:.0f}" for freq in signal["dominant_frequencies_hz"][:3])
            + " Hz}\n"
        )
        f.write(f"\\newcommand{{\\ImageNoisyPSNR}}{{{image['noisy_psnr_db']:.2f}}}\n")
        f.write(f"\\newcommand{{\\ImageLowPassPSNR}}{{{image['low_pass_psnr_db']:.2f}}}\n")
        f.write(f"\\newcommand{{\\ImageNoisyMSE}}{{{image['noisy_mse']:.2f}}}\n")
        f.write(f"\\newcommand{{\\ImageLowPassMSE}}{{{image['low_pass_mse']:.2f}}}\n")
        f.write(f"\\newcommand{{\\ImageLowPassCoeff}}{{{image['low_pass_coefficients_percent']:.2f}}}\n")

    with (OUT / "benchmark_table.tex").open("w", encoding="utf-8") as f:
        f.write("% Auto-generated benchmark table rows\n")
        for row in bench_rows:
            dft_time = "--" if math.isnan(row["DFT_time_ms"]) else f"{row['DFT_time_ms']:.3f}"
            dft_err = "--" if math.isnan(row["DFT_relative_error"]) else f"{row['DFT_relative_error']:.2e}"
            f.write(
                f"{row['N']} & {dft_time} & {row['recursive_FFT_time_ms']:.3f} & "
                f"{row['numpy_FFT_time_ms']:.4f} & {dft_err} & {row['recursive_FFT_relative_error']:.2e} \\\\\n"
            )

    with (OUT / "compression_table.tex").open("w", encoding="utf-8") as f:
        f.write("% Auto-generated compression table rows\n")
        for row in image["compression_rows"]:
            f.write(
                f"{100 * row['energy_retained']:.0f}\\% & {row['coefficients_retained_percent']:.2f}\\% & "
                f"{row['mse']:.2f} & {row['psnr_db']:.2f} \\\\\n"
            )


def main() -> None:
    bench = benchmark_fft()
    signal = signal_experiment()
    image = image_experiment()
    write_outputs(bench, signal, image)
    print("Generated outputs in", OUT)
    print("Signal MSE noisy -> filtered:", f"{signal['noisy_mse']:.4f}", "->", f"{signal['filtered_mse']:.4f}")
    print("Image PSNR noisy -> low-pass:", f"{image['noisy_psnr_db']:.2f}", "->", f"{image['low_pass_psnr_db']:.2f}")


if __name__ == "__main__":
    main()
