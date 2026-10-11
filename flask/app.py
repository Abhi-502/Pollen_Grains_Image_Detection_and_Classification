import os
import zipfile
import numpy as np
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp', 'bmp'}

# Ensure model extraction
model_h5_path = os.path.join(BASE_DIR, 'model1.h5')
if not os.path.exists(model_h5_path):
    zip_path = os.path.join(BASE_DIR, 'model1.zip')
    if os.path.exists(zip_path):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(BASE_DIR)

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max upload

# Load Model
model = None
if os.path.exists(model_h5_path):
    model = load_model(model_h5_path, compile=False)
else:
    print(f"Warning: Model file not found at {model_h5_path}")

labels = [
    'arecaceae', 'anadenanthera', 'arrabidaea', 'cecropia', 'chromolaena',
    'combretum', 'croton', 'dipteryx', 'eucalyptus', 'ficus',
    'guarea', 'hymenaea', 'inga', 'jacaranda', 'machaerium',
    'myrcia', 'ocotea', 'piper', 'protium', 'psidium',
    'schinus', 'solanum', 'urochloa'
]

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_and_predict(filepath):
    """Preprocess image and return top predictions with confidence scores."""
    img = load_img(filepath, target_size=(128, 128))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    raw_preds = model.predict(img_array)[0]
    best_idx = int(np.argmax(raw_preds))
    confidence = float(raw_preds[best_idx]) * 100

    # Top-3 predictions
    top_indices = np.argsort(raw_preds)[::-1][:3]
    top_predictions = [
        {"class": labels[i], "confidence": round(float(raw_preds[i]) * 100, 2)}
        for i in top_indices
    ]

    return labels[best_idx], round(confidence, 2), top_predictions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict-page')
def predict_page():
    return render_template('prediction.html')

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "model_loaded": model is not None,
        "classes_count": len(labels)
    }), 200

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if 'file' not in request.files:
            return render_template('prediction.html', error="No file part in the request.")

        f = request.files['file']
        if f.filename == '':
            return render_template('prediction.html', error="No file selected.")

        if not allowed_file(f.filename):
            return render_template('prediction.html', error="Invalid file format. Allowed formats: PNG, JPG, JPEG, WEBP, BMP.")

        filename = secure_filename(f.filename)
        upload_folder = os.path.join(app.root_path, 'static', 'uploads')
        os.makedirs(upload_folder, exist_ok=True)

        filepath = os.path.join(upload_folder, filename)
        f.save(filepath)

        result, confidence, top_preds = process_and_predict(filepath)
        rel_img_path = os.path.join('static', 'uploads', filename).replace('\\', '/')

        return render_template(
            'prediction.html',
            prediction=result,
            confidence=confidence,
            top_predictions=top_preds,
            img_path=rel_img_path
        )
    except Exception as e:
        app.logger.error(f"Prediction error: {e}")
        return render_template('prediction.html', error=f"An error occurred during prediction: {str(e)}")

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """REST API endpoint for pollen grain image classification."""
    try:
        if 'file' not in request.files:
            return jsonify({"success": False, "error": "No file uploaded under key 'file'"}), 400

        f = request.files['file']
        if f.filename == '':
            return jsonify({"success": False, "error": "Empty filename"}), 400

        if not allowed_file(f.filename):
            return jsonify({"success": False, "error": f"Allowed extensions: {', '.join(ALLOWED_EXTENSIONS)}"}), 400

        filename = secure_filename(f.filename)
        upload_folder = os.path.join(app.root_path, 'static', 'uploads')
        os.makedirs(upload_folder, exist_ok=True)

        filepath = os.path.join(upload_folder, filename)
        f.save(filepath)

        result, confidence, top_preds = process_and_predict(filepath)

        return jsonify({
            "success": True,
            "prediction": result,
            "confidence": confidence,
            "top_predictions": top_preds
        }), 200

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

application = app
