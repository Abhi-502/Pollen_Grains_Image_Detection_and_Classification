# 🌿 Pollen Grain Classification Web App

A deep learning-powered Flask web application that classifies microscope images of pollen grains into 23 plant species using a pretrained Convolutional Neural Network (CNN).

---

## 📸 Demo

Upload a pollen grain image and get an instant prediction with a visual preview.

---

## 🚀 Features

- Upload and classify pollen grain images  
- Real-time predictions using a CNN model (`model1.h5`)  
- Responsive UI with Bootstrap  
- Automatic model extraction from `model1.zip`  

---

## 🧠 Tech Stack

| Layer       | Tools Used              |
|-------------|--------------------------|
| Backend     | Flask, TensorFlow/Keras |
| Frontend    | HTML, CSS, Bootstrap    |
| Model Input | 128×128 RGB images      |

---

## 🏷️ Supported Classes

`arecaceae`, `anadenanthera`, `arrabidaea`, `cecropia`, `chromolaena`, `combretum`, `croton`, `dipteryx`, `eucalyptus`, `ficus`, `guarea`, `hymenaea`, `inga`, `jacaranda`, `machaerium`, `myrcia`, `ocotea`, `piper`, `protium`, `psidium`, `schinus`, `solanum`, `urochloa`

---

## 📁 Project Structure
POLLEN_GRAIN/ ├── app.py # Main Flask app
├── model1.zip # Zipped CNN model 
├── static/ 
│ └── uploads/ # Uploaded images 
├── templates
│ ├── index.html 
│ └── prediction.html
└── README.md


---

## ⚙️ How to Run

1. Clone the repository  
2. Place `model1.zip` in the root directory  
3. Run the app:
   ```bash
   python app.py

