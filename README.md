# 🚗 VisionPark: Smart Vehicle Access & Parking System

VisionPark is an AI-powered smart parking and surveillance system that performs real-time vehicle detection, license plate recognition, access control, and automated alerting.

---

## 🔥 Features

* 🔍 Real-time License Plate Detection (YOLO + OCR)
* 🅿️ Automatic Parking Entry & Exit Logging
* 🚨 Blacklist Detection with Instant WhatsApp Alerts
* ✅ Whitelist-based Access Control
* 📊 Streamlit Dashboard for Monitoring
* 📸 Vehicle Image Capture & Cloud Upload (ImgBB)

---

## 🧠 Tech Stack

* **Python**
* **OpenCV**
* **YOLOv8 (Ultralytics)**
* **Tesseract OCR**
* **Twilio API (WhatsApp Alerts)**
* **Streamlit (Dashboard)**
* **Pandas**
* **ImgBB API (Image Hosting)**

---

## ⚙️ System Architecture

Local System (Laptop)
↓
YOLO Detection + OCR
↓
CSV Database (parking_log.csv)
↓
Streamlit Dashboard (Cloud)
↓
WhatsApp Alerts (Twilio)

---

## 💻 Local Detection System (IMPORTANT)

⚠️ The detection system runs **locally (localhost)** because it requires:

* Webcam access
* Real-time video processing
* OpenCV GUI windows

👉 This part **cannot be deployed directly on Streamlit Cloud**

---

### ▶️ Run Detection (Local)

```bash
python detection.py
```

---

## 🌐 Streamlit Dashboard (Deployed)

The dashboard is deployed on **Streamlit Cloud** and provides:

* Total vehicle count
* Vehicles currently inside
* Entry/Exit logs
* Blacklist & Whitelist view
* Captured vehicle images

---

### ▶️ Run Dashboard Locally

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
VisionPark/
│── detection.py        # Local AI detection system
│── app.py              # Streamlit dashboard
│── parking_log.csv     # Parking database
│── blacklist.csv       # Blacklisted vehicles
│── whitelist.csv       # Allowed vehicles
│── captures/           # Saved vehicle images
│── requirements.txt
│── README.md
│── images/             # Screenshots for README
```

---

## 🔐 Environment Variables

Sensitive keys are NOT stored in code.

Create a `.env` file:

```
TWILIO_SID=your_sid
TWILIO_AUTH=your_token
IMGBB_API_KEY=your_key
```

---

## 🚨 Blacklist Alert System

When a blacklisted vehicle is detected:

* 🚨 WhatsApp alert is triggered
* 📸 Image is captured
* ☁️ Image is uploaded to cloud (ImgBB)
* 📱 Alert + image sent to phone

---

## 📸 Screenshots

### Dashboard Views

<img src="images/dashboard_main.png" width="30%">
<img src="images/dashboard_metrics.png" width="30%">
<img src="images/dashboard_logs.png" width="30%">

### Detection System
![Detection](images/detection.png)

### WhatsApp Alert
![Alert](images/alert.png)

## 📊 Sample Output

**Detected Plate:**

```
KAG2MP9657
```

**System Response:**

```
🚨 BLACKLIST DETECTED
📸 Image captured
📱 WhatsApp Alert Sent
```

---

## 🚀 Future Improvements

* 🔄 Real-time database integration (Firebase / MongoDB)
* 🌍 Fully cloud-based deployment
* 📈 Advanced analytics dashboard
* 🔐 Admin panel for managing vehicles

---

## 👩‍💻 Author

**Diksha Maurya**
Machine Learning & Software Development

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
