from flask import Flask, request, send_file
from flask_cors import CORS
import cv2
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
CORS(app)  # Enable CORS so frontend can call this API

@app.route('/')
def home():
    """Health check endpoint"""
    return {
        "status": "running",
        "message": "MedTech Image Processor API",
        "endpoints": {
            "/process": "POST - Process medical images"
        }
    }

@app.route('/process', methods=['POST'])
def process_image():
    """
    Main endpoint to process medical images
    Expects:
        - image: file (JPG/PNG)
        - phase: string ('arterial' or 'venous')
    Returns:
        - Processed image as file
    """
    try:
        # Get uploaded image from request
        if 'image' not in request.files:
            return {"error": "No image file provided"}, 400
        
        image_file = request.files['image']
        
        # Get phase selection
        phase = request.form.get('phase', 'arterial')
        
        if phase not in ['arterial', 'venous']:
            return {"error": "Invalid phase. Use 'arterial' or 'venous'"}, 400
        
        # Read image file into memory
        image_bytes = image_file.read()
        
        # Convert to numpy array (OpenCV format)
        nparr = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if img is None:
            return {"error": "Invalid image file"}, 400
        
        # Process based on selected phase
        if phase == 'arterial':
            # Arterial phase: Increase contrast
            processed_img = increase_contrast(img)
        else:  # venous
            # Venous phase: Apply Gaussian smoothing
            processed_img = apply_gaussian_blur(img)
        
        # Convert back to image bytes
        success, encoded_image = cv2.imencode('.png', processed_img)
        
        if not success:
            return {"error": "Failed to encode processed image"}, 500
        
        # Send processed image back
        img_io = io.BytesIO(encoded_image.tobytes())
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/png')
    
    except Exception as e:
        return {"error": str(e)}, 500


def increase_contrast(image):
    """
    Simulate arterial phase by increasing image contrast
    
    Args:
        image: OpenCV image (numpy array)
    Returns:
        Contrast-enhanced image
    """
    # Convert to LAB color space
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    
    # Split into L, A, B channels
    l, a, b = cv2.split(lab)
    
    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) to L channel
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    l_enhanced = clahe.apply(l)
    
    # Merge channels back
    enhanced_lab = cv2.merge([l_enhanced, a, b])
    
    # Convert back to BGR
    enhanced_image = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)
    
    return enhanced_image


def apply_gaussian_blur(image):
    """
    Simulate venous phase by applying Gaussian smoothing
    
    Args:
        image: OpenCV image (numpy array)
    Returns:
        Smoothed image
    """
    # Apply Gaussian blur
    # Kernel size (15, 15) - larger = more blur
    # sigmaX=0 means it's calculated from kernel size
    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
    
    return blurred_image


if __name__ == '__main__':
    # Run the Flask app
    # Use host='0.0.0.0' to make it accessible externally
    app.run(host='0.0.0.0', port=7860, debug=False)