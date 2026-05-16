# Gamma.ai Presentation Generation Prompt

Create a professional academic presentation for a MATH307 Numerical Analysis final project.

Project title: **Fast Fourier Transform (FFT) Implementation and Its Applications**

Team:
- Ali Ashraf, 202301812
- Abdelrahman Mohamed, 202300056
- Ahmed Mohamady, 202301826

## Global Style Instructions

Create exactly **10 slides**. Use a clean modern academic theme with strong visual hierarchy, readable equations, and concise text. Do not remove important content; compress related ideas into combined slides. Avoid generic AI-looking filler graphics. Use visuals directly related to Fourier analysis, numerical methods, frequency spectra, signal denoising, image processing, matrices, algorithms, and experimental plots.

Use a white or very light background, charcoal text, deep blue as the main accent, and one secondary color for frequency-domain highlights. Keep each slide presentation-friendly: short bullets, large plots, readable formulas, and clear speaker flow.

Use these generated project assets where appropriate:
- `Report/generated/runtime_comparison.png`
- `Report/generated/signal_spectrum.png`
- `Report/generated/signal_filtering.png`
- `Report/generated/image_fft_processing.png`
- `Report/generated/compression_tradeoff.png`

Key numerical results to include:
- Signal noisy MSE: 0.1579
- Signal filtered MSE: 0.0375
- Signal improvement: 6.24 dB
- Dominant detected frequencies: 50 Hz, 120 Hz, 300 Hz
- Image noisy PSNR: 20.65 dB
- Image low-pass filtered PSNR: 21.99 dB
- Image noisy MSE: 560.29
- Image low-pass filtered MSE: 411.54
- Low-pass image mask retained: 8.43% of frequency coefficients
- Compression at 98% spectral energy: 2.99% coefficients, 25.12 dB PSNR
- Compression at 99% spectral energy: 6.13% coefficients, 28.13 dB PSNR

## Required 10-Slide Structure

### Slide 1: Title, Team, and Project Snapshot
Purpose: Introduce the project and immediately show what was built.
Key bullets:
- Fast Fourier Transform (FFT) Implementation and Its Applications
- MATH307 Numerical Analysis final project
- Goal: compute frequency representations efficiently and apply them to signal/image processing
- Deliverables: mathematical derivation, Python implementation, experiments, plots, final report, demo-ready output
Suggested visual:
- Subtle waveform-to-spectrum background or small split image showing time-domain signal and frequency spectrum.
Presenter emphasis:
- This is both a numerical-method analysis and a working implementation project.

### Slide 2: Problem Motivation and Course/Rubric Alignment
Purpose: Explain why the project matters and how it satisfies the requirements.
Key bullets:
- Direct DFT is mathematically useful but costs \(O(N^2)\)
- FFT computes the same transform in \(O(N\log N)\)
- Applications: denoising, spectral analysis, image filtering, compression, AI preprocessing
- Rubric coverage: clear idea, methodology, code/simulation, comparison, parameter effects, results analysis, presentation, working output
Suggested visual:
- Compact checklist graphic beside a mini complexity comparison.
Presenter emphasis:
- The project is designed around the professor’s expectations: theory, implementation, comparison, analysis, and demo.

### Slide 3: Mathematical Foundation: DFT and Inverse DFT
Purpose: Present the core numerical problem.
Key bullets:
- DFT:
  \(X_k=\sum_{n=0}^{N-1}x_n e^{-i2\pi kn/N}\)
- Inverse DFT:
  \(x_n=\frac{1}{N}\sum_{k=0}^{N-1}X_k e^{i2\pi kn/N}\)
- Matrix view: \(\mathbf{X}=W_N\mathbf{x}\)
- Direct DFT requires dense summation for every frequency coefficient
Suggested visual:
- Matrix-vector multiplication diagram plus signal-to-spectrum arrow.
Presenter emphasis:
- The transform is exact, but direct computation becomes expensive as data grows.

### Slide 4: FFT Methodology and Complexity
Purpose: Explain the numerical method and why it is faster.
Key bullets:
- Split input into even and odd samples
- \(X_k=E_k+\omega_N^kO_k\)
- \(X_{k+N/2}=E_k-\omega_N^kO_k\)
- Recurrence: \(T(N)=2T(N/2)+O(N)\)
- Complexity improves from \(O(N^2)\) to \(O(N\log N)\)
Suggested visual:
- Butterfly diagram or recursion tree with even/odd split.
Animation suggestion:
- Reveal the split, then the two butterfly equations, then the complexity result.
Presenter emphasis:
- FFT is not an approximation; it reorganizes the same DFT computation efficiently.

### Slide 5: Implementation and Validation Workflow
Purpose: Show the project’s working code and validation plan.
Key bullets:
- Implemented direct DFT from definition
- Implemented recursive radix-2 Cooley--Tukey FFT
- Implemented inverse FFT using conjugate identity
- Validated against NumPy FFT using relative error
- Generated report-ready figures and tables from Python
Suggested visual:
- Workflow diagram:
  Input signal/image -> DFT/FFT -> NumPy validation -> filtering/compression -> metrics/plots -> report/demo
Suggested mini code visual:
- Include a small snippet or pseudo-code block of recursive FFT, but keep it readable.
Presenter emphasis:
- The project has reproducible working output, not only theoretical discussion.

### Slide 6: Benchmark Results: Runtime and Numerical Accuracy
Purpose: Combine performance comparison and correctness.
Key bullets:
- Tested complex random signals for \(N=16\) to \(2048\)
- Compared direct DFT, custom recursive FFT, and NumPy FFT
- Direct DFT grows quickly; FFT scales much better
- Recursive FFT relative error stayed near \(10^{-15}\)
- NumPy FFT is fastest because it uses optimized compiled routines
Suggested visual:
- Main visual: `runtime_comparison.png`
- Add small metric callout: “FFT error ≈ machine precision”
Suggested table callout:
- Include representative rows: \(N=512\), DFT 11.915 ms, recursive FFT 4.503 ms, NumPy FFT 0.0201 ms
Presenter emphasis:
- This slide proves both efficiency and accuracy.

### Slide 7: Signal Processing Experiment: Spectrum and Denoising
Purpose: Show practical one-dimensional FFT application.
Key bullets:
- Clean signal contains 50 Hz and 120 Hz components
- Added 300 Hz interference plus Gaussian noise
- FFT detected dominant frequencies: 50 Hz, 120 Hz, 300 Hz
- Low-pass cutoff at 160 Hz removed high-frequency interference
- MSE improved from 0.1579 to 0.0375, a 6.24 dB improvement
Suggested visuals:
- Use `signal_spectrum.png` and `signal_filtering.png` side by side.
Suggested layout:
- Left: frequency spectrum with cutoff.
- Right: clean/noisy/filtered waveform.
Presenter emphasis:
- FFT turns denoising into a clear frequency-domain masking problem.

### Slide 8: Image Processing Experiment: 2D FFT Filtering and Feature Emphasis
Purpose: Show two-dimensional FFT application and image metrics.
Key bullets:
- 2D FFT extends frequency analysis to images
- Low frequencies represent smooth structure
- High frequencies represent edges, texture, and noise
- Low-pass filtering improved PSNR from 20.65 dB to 21.99 dB
- Image MSE improved from 560.29 to 411.54
- Filter retained only 8.43% of centered frequency coefficients
Suggested visual:
- Use `image_fft_processing.png` as the dominant visual.
Presenter emphasis:
- Discuss the clean image, noisy image, FFT magnitude, low-pass denoising, high-pass edge emphasis, and error panel.

### Slide 9: Compression, Parameter Effects, and Error/Stability Analysis
Purpose: Compress the remaining analysis requirements into one strong technical slide.
Key bullets:
- Parameter effects studied: signal length \(N\), filter cutoff, image mask radius, retained spectral energy
- Compression tradeoff:
  98% energy -> 2.99% coefficients, 25.12 dB PSNR
  99% energy -> 6.13% coefficients, 28.13 dB PSNR
- FFT numerical error stayed near machine precision
- Filtering error depends mainly on modeling choices: too low cutoff removes useful signal; too high cutoff keeps noise
- Low-pass filters denoise but may blur; high-pass filters reveal edges but may amplify noise
Suggested visual:
- Use `compression_tradeoff.png`
- Add a small two-column note: “Numerical error” vs “modeling/filtering error”
Presenter emphasis:
- This slide shows critical analysis, not just positive results.

### Slide 10: Demo Readiness, Conclusion, and References
Purpose: End with reproducibility, final insights, and citations.
Key bullets:
- Demo command: `python experiments/fft_experiments.py`
- Outputs saved in `Report/generated/`
- Final report imports generated figures and computed metrics
- Main conclusion: FFT reduces DFT complexity from \(O(N^2)\) to \(O(N\log N)\) while preserving accuracy
- Applications confirmed: runtime acceleration, signal denoising, image filtering, edge emphasis, compression
Suggested visual:
- Three takeaway cards: Speed, Accuracy, Applications
- Small reproducibility flow: code -> figures/tables -> report/presentation
References:
- Cooley and Tukey, 1965
- Oppenheim and Schafer, Discrete-Time Signal Processing
- Smith, The Scientist and Engineer's Guide to Digital Signal Processing
- Gonzalez and Woods, Digital Image Processing
- NumPy FFT documentation
Presenter emphasis:
- Close by connecting mathematical structure to practical scientific computing and AI preprocessing.

## Extra Gamma Instructions

Do not create more than 10 slides. Do not delete major content; combine it intelligently. Keep equations readable and avoid overcrowding. For slides 6-9, make the plots the main visual and use short callouts for interpretation. Avoid stock illustrations unless they directly show signals, spectra, matrices, algorithms, or scientific computing.
