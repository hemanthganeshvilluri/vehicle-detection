# 🚗 Vehicle Detection (5 Classes) using YOLOv8n

This project focuses on **vehicle detection and classification** using **Ultralytics YOLOv8n**. The model is trained on a dataset containing **5 vehicle classes** and deployed using **FastAPI** for video processing.

---

## 📌 Project Overview

- 🔍 Detects and classifies vehicles into 5 classes  
- ⚡ Built using **YOLOv8n (Ultralytics)**  
- 🎥 Currently supports **video input processing**  
- 🚀 Backend deployed using **FastAPI**  
- 🔜 Future scope: **Live camera (real-time detection)**  

---

## 📂 Dataset

- 📊 Dataset Source:  
  https://www.kaggle.com/datasets/hammadjavaid/vehicle-object-detection-dataset-5-classes  

- Classes:
  - Bus  
  - Car  
  - Pickup  
  - Truck  
  - Van  

---

## 🧠 Model Training

- 🧪 Training done on **Kaggle**
- 🔗 Notebook Link:  
  https://www.kaggle.com/code/hemanthganeshvilluri/vehicle-detection  

- Model Used:
  - `yolov8n` (lightweight and fast)

---

## ⚙️ Tech Stack

- **Ultralytics YOLOv8**
- **FastAPI**
- **OpenCV (cv2)**
- **Python**

---

## 🏗️ Project Structure

```
vehicle-detection/
│── templates/           # HTML templates (if used for UI)
│── weights/             # Trained YOLOv8 model weights
│── app.py               # FastAPI application
│── requirements.txt     # Dependencies
│── README.md            # Project documentation
```

---

## 🚀 How It Works

1. Upload or provide a video  
2. Frames are processed using OpenCV  
3. YOLOv8 detects vehicles in each frame  
4. Bounding boxes and labels are added  
5. Output video is generated  

---

## ▶️ Running the Project

### 1. Clone the Repository
```bash
git clone https://github.com/hemanthganeshvilluri/vehicle-detection.git
cd vehicle-detection
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run FastAPI Server
```bash
uvicorn app:app --reload
```

### 4. Open in Browser
```
http://127.0.0.1:8000
```

---

## 📈 Features

- ✅ Multi-class vehicle detection  
- ✅ Fast and lightweight model (YOLOv8n)  
- ✅ Video processing support  
- ✅ FastAPI backend  

---

## 🔮 Future Improvements

- 🎥 Live camera detection  
- 🌐 Web UI improvements  
- ☁️ Cloud deployment  
- 📊 Model performance optimization  

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📧 Contact

**Hemanth Ganesh Villuri**  
📩 hemanthganeshvilluri@gmail.com  
