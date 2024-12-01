# Arabic Sign Language Detection and Conversion System

### **Overview**
This project is an object detection and computer vision system that converts Arabic sign language into text using the YOLO (You Only Look Once) model. It is designed as a tool for improving communication between deaf and mute individuals and the general public by translating hand signs into readable text. 

The project includes:
1. A **dataset** of 24,000 images of Arabic hand signs.
2. A trained YOLO model for sign language detection.
3. A **Flask-based backend** for deploying the model.
4. A **user-friendly website** to facilitate communication between users.

---

### **Key Features**
- **Dataset Creation**: A dataset of 24,000 annotated images of Arabic hand signs. 
- **YOLO Object Detection**: Model implementation for high-speed and accurate detection of Arabic hand signs.
- **Real-time Translation**: Converts Arabic sign language gestures into text (letters and words).
- **Web Application**: Intuitive interface to bridge communication gaps for deaf and mute users.

---

### **Project Structure**
```plaintext
Arabic-Sign-Language-Detection/
│
├── dataset/
│   ├── images/            # Dataset images (24,000 samples)
│   ├── annotations/       # Annotations in YOLO format
│   └── data_split/        # Train, Validation, and Test sets
│
├── model/
│   ├── yolov5/            # YOLOv5 model implementation
│   └── trained_weights/   # Trained model weights
│
├── app/
│   ├── static/            # Static files (CSS, JS, Images)
│   ├── templates/         # HTML templates
│   ├── app.py             # Flask backend
│   └── requirements.txt   # Python dependencies
│
├── website/
│   ├── index.html         # Main website page
│   ├── styles.css         # CSS for the website
│   ├── script.js          # JS for frontend functionality
│
├── README.md              # Project documentation
└── LICENSE                # License file
