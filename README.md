# 🌿 Pollen Grain Image Detection & Classification

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-black.svg)](https://flask.palletsprojects.com/)
[![TensorFlow](https://img.shields.io/badge/Deep%20Learning-TensorFlow%2FKeras-orange.svg)](https://tensorflow.org/)
[![Docker](https://img.shields.io/badge/Container-Docker-2496ED.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An end-to-end deep learning system and web application for automated microscopic detection and classification of pollen grains across **23 plant species** using Convolutional Neural Networks (CNNs).

---

## 📸 Overview & Demo

Identifying pollen morphology is critical in aerobiology, botany, allergy diagnostics, and paleoecology. This project delivers an automated pipeline that takes microscopic images of pollen grains, normalizes them, and predicts the exact botanical taxa with confidence ratings and top-k candidate rankings.

---

## 🚀 Key Features

- **Microscopic Image Classification**: Accurately classifies pollen grains across 23 distinct botanical species.
- **Real-Time Predictions & Confidence Scoring**: Outputs top-1 classification along with confidence percentages and top-3 ranked alternatives.
- **Interactive Web Interface**: Responsive UI with image drag-and-drop preview and dynamic prediction result cards.
- **RESTful API**: `/api/predict` endpoint for headless integration, automated laboratory pipelines, and mobile apps.
- **Containerized Deployment**: Ready-to-deploy `Dockerfile` and `docker-compose.yml` powered by Gunicorn production WSGI server.
- **Automated Extraction**: Automatic model extraction from compressed artifacts (`model1.zip`) during startup.

---

## 🧠 Tech Stack

| Layer | Tools & Technologies |
|---|---|
| **Deep Learning** | TensorFlow / Keras (CNN), NumPy, Pillow |
| **Backend & API** | Flask 2.x, Gunicorn, Werkzeug |
| **Frontend** | HTML5, CSS3, JavaScript, FontAwesome |
| **DevOps & CI** | Docker, Docker Compose, GitHub Actions |

---

## 🏷️ Supported Botanical Classes (23 Species)

The model is trained to identify pollen grains from 23 botanical families and genera:

```
• Arecaceae       • Anadenanthera   • Arrabidaea      • Cecropia
• Chromolaena     • Combretum       • Croton          • Dipteryx
• Eucalyptus      • Ficus           • Guarea          • Hymenaea
• Inga            • Jacaranda       • Machaerium      • Myrcia
• Ocotea          • Piper           • Protium         • Psidium
• Schinus         • Solanum         • Urochloa
```

---

## 📁 Repository Structure

```text
├── .github/workflows/
│   └── ci.yml               # Automated CI workflow
├── data/                    # Dataset containing pollen grain sample images
├── flask/
│   ├── static/
│   │   ├── css/main.css     # UI styling & responsive layouts
│   │   ├── images/          # Background assets
│   │   ├── js/main.js       # Frontend interactivity
│   │   └── uploads/         # Upload staging directory
│   ├── templates/
│   │   ├── index.html       # Home landing page with carousel
│   │   └── prediction.html  # Interactive classifier page
│   ├── app.py               # Flask application & REST API routes
│   ├── class_labels.txt     # List of class indices and labels
│   ├── model1.zip           # Compressed trained CNN model
│   └── pollen_grain_classification.ipynb # Training & evaluation notebook
├── .dockerignore
├── .gitignore
├── docker-compose.yml       # Multi-container orchestration
├── Dockerfile               # Production container image definition
├── requirements.txt         # Project Python dependencies
└── README.md
```

---

## ⚡ Quick Start

### Option 1: Local Environment

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Abhi-502/Pollen_Grains_Image_Detection_and_Classification.git
   cd Pollen_Grains_Image_Detection_and_Classification
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application:**
   ```bash
   python flask/app.py
   ```
   Open [http://localhost:5000](http://localhost:5000) in your browser.

---

### Option 2: Docker Setup

Run the application inside an isolated Docker container:

```bash
docker build -t pollen-classifier .
docker run -p 5000:5000 pollen-classifier
```

Or using **Docker Compose**:
```bash
docker compose up -d
```
Access the application at [http://localhost:5000](http://localhost:5000).

---

## 🔌 API Reference

### 1. Classify Image (`POST /api/predict`)

Send a `multipart/form-data` request with an image file:

```bash
curl -X POST http://localhost:5000/api/predict \
  -F "file=@data/arecaceae_01.jpg"
```

**Response:**
```json
{
  "success": true,
  "prediction": "arecaceae",
  "confidence": 98.42,
  "top_predictions": [
    { "class": "arecaceae", "confidence": 98.42 },
    { "class": "syagrus", "confidence": 1.15 },
    { "class": "ficus", "confidence": 0.28 }
  ]
}
```

### 2. Health Check (`GET /health`)

```bash
curl http://localhost:5000/health
```

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "classes_count": 23
}
```

---

## 👥 Contributors & Contact

- **Illuri Abhi** ([GitHub: @Abhi-502](https://github.com/Abhi-502) | [Email](mailto:23091a0502@rgmcet.edu.in))
- **Gandragoli Upendra**
- **Pitta Murali**
- **Mukesh Kumar**

---

## 📄 License

This project is licensed under the MIT License.
