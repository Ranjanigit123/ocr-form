from flask import Flask, render_template, request, jsonify
from PIL import Image
import pytesseract
import io

app = Flask(__name__)

# Tesseract OCR configuration (change this according to your installation path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Route to handle the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the OCR process
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        img_bytes = file.read()
        image = Image.open(io.BytesIO(img_bytes))
        text = pytesseract.image_to_string(image)
        return jsonify({'text': text})


if __name__ == '__main__':
    app.run(debug=True)