# License Plate Recognizer 🚘🔍

This project is an AI-powered License Plate Recognition (LPR) system that detects vehicles and extracts license plate numbers from images or video frames using YOLOv5 and Optical Character Recognition (OCR).

---

## 📁 Project Structure

Car_num/
├── yolov5/ # YOLOv5 cloned repo (ignored in Git)
├── license_plate_notebook.ipynb
├── cropped_plates/ # Output directory for cropped license plates
├── annotated_plates/ # Annotated plate images
├── data/ # Raw image/video data
├── utils/ # Utility functions
├── README.md


---

## 🚀 Features

- Detects cars and localizes license plates using YOLOv5
- Crops detected license plates
- Applies OCR to read text from plates
- Outputs bounding box images and extracted text
- Easy-to-use Jupyter Notebook for experimentation

---

## 🧠 Technologies Used

- Python
- OpenCV
- YOLOv5 (object detection)
- EasyOCR / Tesseract (OCR)
- NumPy, Matplotlib, Pandas

---

## ⚙️ Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Saurabh-Zarekar/License_Plate_Recognizer.git
   cd License_Plate_Recognizer
2. **Create a virtual environment and activate it**:
python -m venv venv
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate

3. **Install dependencies**:
pip install -r yolov5/requirements.txt
pip install easyocr opencv-python matplotlib pandas

4. **Launch Jupyter Notebook**:
jupyter notebook

