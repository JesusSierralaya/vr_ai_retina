# 🧠 Immersive VR + AI for Early Alzheimer's Detection

This project explores a novel approach to **early Alzheimer's disease detection** using **retinal imaging**, **artificial intelligence (AI)**, and **immersive virtual reality (VR)**. It aims to visualize and analyze 3D OCT retinal data to reveal subtle biomarkers of early-stage Alzheimer’s, enabling more intuitive diagnosis through an interactive VR environment.

## 🔬 Background

Alzheimer’s disease is difficult to detect in its earliest stages. However, research shows that retinal biomarkers may indicate early pathological changes. While **Optical Coherence Tomography (OCT)** can scan retinal layers, current tools lack advanced 3D visualization and pattern recognition capabilities. This project bridges that gap using:

- **VR-based exploration** of OCT data
- **AI models** trained on retinal biomarkers
- Integration with **commercial VR headsets**

> *Innovation: This is the first approach to combine 3D VR retinal visualization with AI-driven analysis for early-stage Alzheimer’s detection.*

## 📁 Project Structure
.
├── objects/ # 3D object models (retinal surfaces, etc.)
├── shaders/ # GLSL shaders for lighting and texture rendering
├── surfaces_data/ # Layered surface data (OCT scans)
├── textures/ # Texture data for rendering
├── camera.py # Camera system for VR navigation
├── config.py # Project configuration and constants
├── light.py # Lighting setup (e.g., Phong illumination)
├── main.py # Entry point to run the VR app
├── mesh.py # Scene mesh handling
├── model.py # 3D object definitions
├── scene.py # Scene management and rendering pipeline
├── shader_program.py # Shader program handling
├── texture.py # Texture loading utilities
├── vao.py / vbo.py # OpenGL VAO and VBO management
└── README.md # You're here!


## 🧪 Methods

### 1. VR System Development (Python + OpenGL)
- Renders 3D OCT retinal scans.
- Enables user interaction for exploring potential Alzheimer's biomarkers.
- Compatible with commercial VR headsets (e.g., Oculus, HTC Vive).

### 2. AI Model Training (Planned)
- Trains deep learning & classical ML models on retinal biomarkers (e.g., layer thickness, fractal dimension).
- Goal: Predict probability of early-stage Alzheimer’s.
- AUC target: **> 0.85**

## 🖥️ Dependencies

- Python 3.x
- OpenGL / PyOpenGL
- GLFW / SDL2
- NumPy
