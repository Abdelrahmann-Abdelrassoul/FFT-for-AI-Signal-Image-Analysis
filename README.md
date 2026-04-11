# 🚀 Fast Fourier Transform (FFT) in Numerical Analysis  
### 📊 Applications in Signal Processing & AI-Based Image Processing  

---

## 📌 Project Overview

This project is developed for **Math 307 – Numerical Analysis** and focuses on the implementation, analysis, and application of the **Fast Fourier Transform (FFT)**.

The FFT is a fundamental numerical algorithm used to efficiently compute the **Discrete Fourier Transform (DFT)**, reducing computational complexity from:

- **O(N²)** → using DFT  
- **O(N log N)** → using FFT  

This project bridges **analytical methods (DFT)** and **numerical methods (FFT)** and demonstrates their importance in real-world computational and AI systems.

---

## 🎯 Objectives

- Implement **DFT (analytical method)** and **FFT (numerical method)**
- Compare performance and computational complexity
- Analyze numerical accuracy and efficiency
- Apply FFT to real-world problems
- Investigate the effect of parameters (signal size, noise, etc.)
- Explore **AI-related applications**, especially in image processing

---

## 🧠 Core Concepts

- Fourier Transform
- Discrete Fourier Transform (DFT)
- Fast Fourier Transform (FFT)
- Computational Complexity Analysis
- Numerical Accuracy & Stability
- Signal & Image Processing

---

## 🔬 Methodology

### 1. Analytical Method – DFT
- Direct implementation of the DFT formula
- Used as a baseline for comparison
- High computational cost: **O(N²)**

---

### 2. Numerical Method – FFT
- Recursive decomposition (divide & conquer)
- Efficient computation: **O(N log N)**
- Implemented from scratch and compared with built-in libraries

---

### 3. Performance Analysis
- Runtime comparison between DFT and FFT
- Scalability analysis with increasing input size
- Visualization using plots

---

## 📊 Applications

### 🔹 1. Signal Filtering & Noise Reduction
- Transform signal to frequency domain
- Remove unwanted frequencies
- Reconstruct clean signal using inverse FFT

---

### 🔹 2. Frequency Analysis
- Detect dominant frequencies in signals
- Applications in:
  - Audio processing
  - Biomedical signals
  - Communication systems

---

### 🤖 3. Image Processing (AI-Focused)

This is the **main highlight of the project**.

Using **2D FFT**, images are transformed into the frequency domain for advanced processing:

#### ✔ Noise Reduction
- Remove high-frequency noise using low-pass filters

#### ✔ Edge Detection
- Enhance edges using high-frequency components

#### ✔ Image Compression
- Discard less important frequency components

---

### 💡 Why This Matters for AI

FFT plays a critical role in modern AI and Computer Vision:

- Feature extraction for machine learning models  
- Preprocessing for deep learning pipelines  
- Efficient handling of large image data  
- Frequency-domain filtering for better model performance  

👉 FFT is widely used in:
- CNN preprocessing  
- Image denoising  
- Pattern recognition systems  

---

## 📈 Experiments & Analysis

- Runtime comparison (DFT vs FFT)
- Effect of signal size (N)
- Noise impact on signal reconstruction
- Image filtering quality comparison
- Accuracy vs performance trade-offs

---

## 🛠️ Technologies Used

- **Python**
- NumPy
- Matplotlib
- OpenCV / PIL for image processing

---

## 📚 Deliverables

- ✔ Mathematical derivations  
- ✔ Python implementations  
- ✔ Simulation results and plots  
- ✔ Comparative analysis  
- ✔ Final report (LaTeX)  
- ✔ Presentation slides  

---

## 👥 Team Members

- Abdelrahman Abdelrassoul — ID: 202300056
- Ahmed Mohammady — ID: 202301826
- Ali Ashraf — ID: 202301812

---

## 📌 Conclusion

This project demonstrates how numerical methods like FFT significantly improve computational efficiency while enabling powerful applications in signal processing and AI.

By combining theory, implementation, and real-world applications, the project highlights the importance of FFT as a cornerstone algorithm in modern computational science.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## ⭐ Notes

- This project is part of an academic course (Math 307)
- Code is written for educational and demonstration purposes
- Designed to showcase both **numerical analysis concepts and AI relevance**
