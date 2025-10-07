# MedTech Image Processor

A full-stack web application for simulating medical image phase processing (arterial and venous phases).

## 🎯 What It Does

This application allows users to:
- Upload a 2D medical image (JPG/PNG format)
- Select a phase simulation:
  - **Arterial Phase**: Increases image contrast using CLAHE algorithm
  - **Venous Phase**: Applies Gaussian smoothing to the image
- View the original and processed images side-by-side

## 🚀 Demo

**Live Application**: [https://ravijagunawardena.github.io/medtech-image-processor/frontend/]

## 🏗️ Architecture

- **Frontend**: Static HTML/CSS/JavaScript (hosted on GitHub Pages)
- **Backend**: Python Flask API with OpenCV (hosted on Hugging Face Spaces)
- **Communication**: RESTful API with image file upload

## 📁 Project Structure

```
medtech-image-processor/
├── frontend/
│   └── index.html          # Complete frontend application
├── backend/
│   ├── app.py              # Flask API server
│   └── requirements.txt    # Python dependencies
└── README.md
```

## 🛠️ Setup Instructions

### Backend Setup (Hugging Face Spaces)

1. Create a new Space on Hugging Face:
   - Go to https://huggingface.co/spaces
   - Click "Create new Space"
   - Choose "Gradio" SDK (or Docker)
   - Name it (e.g., "medtech-image-processor")

2. Upload backend files:
   - Upload `app.py` to the Space
   - Upload `requirements.txt` to the Space

3. The Space will automatically deploy. Note the URL (e.g., https://username-spacename.hf.space)

### Frontend Setup (GitHub Pages)

1. Create a GitHub repository

2. Add frontend files:
   ```bash
   mkdir frontend
   # Add index.html to frontend folder
   ```

3. Update the backend URL in `index.html`:
   - Open `frontend/index.html`
   - Find line: `const BACKEND_URL';`
   - Replace with your actual Hugging Face Space URL

4. Enable GitHub Pages:
   - Go to repository Settings → Pages
   - Source: Deploy from branch
   - Branch: main, folder: /frontend
   - Save

5. Access your app at: `https://username.github.io/repo-name/`

## 💻 Local Development

### Backend
```bash
cd backend
pip install -r requirements.txt
python app.py
# Server runs on http://localhost:7860
```

### Frontend
Simply open `frontend/index.html` in a browser, or use a local server:
```bash
cd frontend
python -m http.server 8000
# Open http://localhost:8000
```

## 🔧 Technologies Used

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Backend**: Python, Flask, OpenCV, NumPy
- **Image Processing**: 
  - CLAHE (Contrast Limited Adaptive Histogram Equalization)
  - Gaussian Blur

## 📝 API Documentation

### POST /process

Process a medical image with selected phase simulation.

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body:
  - `image`: Image file (JPG/PNG)
  - `phase`: String ("arterial" or "venous")

**Response:**
- Success: Returns processed image file (PNG)
- Error: JSON with error message

**Example using curl:**
```bash
curl -X POST \
  -F "image=@sample.jpg" \
  -F "phase=arterial" \
  https://your-space.hf.space/process \
  --output processed.png
```

## 🎨 Features

- ✅ Clean, modern UI with gradient design
- ✅ Drag-and-drop file upload
- ✅ Real-time phase selection
- ✅ Side-by-side image comparison
- ✅ Loading indicators
- ✅ Error handling
- ✅ Responsive design (mobile-friendly)
- ✅ CORS-enabled API

## ⚠️ Notes

- Image processing is performed entirely on the backend (Python)
- No client-side image manipulation
- Supported formats: JPG, PNG
- Maximum recommended image size: 10MB

## 📄 License

This project is for educational/demonstration purposes.
