# Fast Fourier Transform (FFT) in Numerical Analysis

## Project Overview

This project focuses on the implementation and analysis of the Fast Fourier Transform (FFT) and its comparison with the Discrete Fourier Transform (DFT). The FFT reduces computational complexity from \(O(N^2)\) to \(O(N log N)\), making it suitable for large-scale problems.

---

## Objectives

- Implement DFT and FFT
- Compare performance and computational complexity
- Analyze numerical accuracy and efficiency
- Apply FFT to signal and image processing tasks

---

## Core Concepts

- Fourier Transform
- Discrete Fourier Transform (DFT)
- Fast Fourier Transform (FFT)
- Computational Complexity
- Signal and Image Processing

---

## Methodology

### DFT (Baseline)
- Direct implementation
- Complexity: \(O(N^2)\)

### FFT
- Recursive divide-and-conquer approach
- Complexity: \(O(N \log N)\)

### Analysis
- Runtime comparison
- Scalability with input size

---

## Applications

### Signal Filtering and Noise Reduction
- Transform signals to frequency domain
- Remove noise components
- Reconstruct signal using inverse FFT

### Frequency Analysis
- Identify dominant frequencies in signals
- Used in audio, biomedical, and communication systems

### Image Processing
- Apply 2D FFT on images
- Noise reduction (low/high-pass filtering)
- Edge enhancement
- Image compression

---

## Experiments

| Experiment                     | Description                                  |
|------------------------------|----------------------------------------------|
| Runtime Comparison           | DFT vs FFT performance                       |
| Signal Size Scaling          | Effect of increasing \(N\)                   |
| Noise Analysis               | Impact on signal reconstruction              |
| Image Filtering              | Quality comparison in frequency domain       |
| Accuracy vs Performance      | Trade-offs between methods                   |

---

## Technologies

| Technology | Purpose                      |
|-----------|------------------------------|
| Python    | Implementation               |
| NumPy     | Numerical computations       |
| Matplotlib| Visualization                |
| OpenCV/PIL| Image processing             |

---

## Project Outputs

- Final report: `Report/FinalReport.tex` and `Report/FinalReport.pdf`
- Presentation: `Presentation/`
- Experiment code: `experiments/fft_experiments.py`
- Generated plots and result tables: `Report/generated/`

---

## Reproduce Results

Run the experiment script from the repository root:

```bash
python experiments/fft_experiments.py
```

This regenerates the benchmark results, signal filtering plots, image processing plots, and compression analysis used in the final report.
