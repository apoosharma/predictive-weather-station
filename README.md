# Predictive Weather Station 🌦️
### ESP32 + Machine Learning + Flask API

A real-time IoT + ML project where an ESP32 microcontroller fetches live 
weather data from the internet, and a Machine Learning model predicts the 
next temperature — all connected through a REST API built with Flask.

---

## 📌 Project Overview

Most weather stations just display current data. This one **predicts** it.

The ESP32 continuously fetches live temperature and humidity from 
OpenWeatherMap's REST API. That data is logged, used to train a Linear 
Regression model in Python, and the trained model is deployed as a Flask 
API. The ESP32 then queries this API in real time and receives a predicted 
temperature back — completing a full IoT + ML pipeline on real hardware.

---

## 🔧 Tech Stack

| Layer | Technology |
|---|---|
| Hardware | ESP32 (CP2102, 38-pin) |
| Embedded | Arduino IDE, C++ |
| Data Source | OpenWeatherMap REST API |
| ML Model | Linear Regression (Scikit-learn) |
| Backend | Python, Flask |
| Data Format | JSON |
| Communication | HTTP GET requests |

---

## 🏗️ System Architecture

OpenWeatherMap API
↓
ESP32 (WiFi)
↓
Fetches temp, humidity, timestamp
↓
Logs data → weather_data.csv
↓
Python trains Linear Regression model
↓
Flask deploys model as REST API
↓
ESP32 queries Flask → gets predicted temp
↓
Displays on Serial Monitor in real time
---

## 📁 Project Structure

predictive-weather-station/
|── DHT11                   # DHT11.code into ESP32
├── app.py                  # Flask API with trained ML model
├── weather_data.py         # Model training + evaluation + plot
├── weather_data.csv        # Collected real weather data
└── README.md
---

## ⚙️ How It Works

### Step 1 — ESP32 fetches live weather
ESP32 connects to WiFi and sends an HTTP GET request to OpenWeatherMap API.
It parses the JSON response and extracts temperature, humidity, and timestamp.

### Step 2 — Data collection
Data is logged in CSV format via Serial Monitor:

1781131042, 29.35, 63.00
1781131642, 29.12, 65.00

### Step 3 — ML model training
A Linear Regression model is trained on the collected data.
- Features: timestamp, current temperature, humidity
- Target: next temperature reading
- Result: **MAE of 0.19°C** on training data

### Step 4 — Flask API deployment

The trained model is deployed as a REST API endpoint:
GET /predict?timestamp=1781131042&temp=29.35&humidity=63
Response: {"predicted_temp": 29.12}

### Step 5 — ESP32 queries Flask
ESP32 sends live sensor data to the Flask API and receives the predicted 
temperature back in real time, completing the full pipeline.

---

## 🚀 How to Run

### Prerequisites
- ESP32 dev board (CP2102)
- Arduino IDE with ESP32 board support
- Python 3.x
- OpenWeatherMap free API key

### 1. Clone the repo
```bash
git clone https://github.com/apoosharma/predictive-weather-station.git
cd predictive-weather-station
```

### 2. Install Python dependencies
```bash
pip install flask scikit-learn pandas numpy matplotlib
```

### 3. Collect data (optional — sample data included)
- Flash `DHT11_code.ino` to ESP32
- Update WiFi credentials and API key
- Let it run for a few hours
- Save Serial Monitor output as `weather_data.csv`

### 4. Train the model and check accuracy
```bash
python weather_prediction.py
```

### 5. Run Flask API
```bash
python app.py
```
Note your laptop's local IP (shown in terminal) and update it in the Arduino code.

### 6. Flash final ESP32 code
- Update WiFi credentials, API key, and Flask server IP in `DHT11_code.ino`
- Upload to ESP32
- Open Serial Monitor at 115200 baud

---

## 📊 Sample Output
Connecting to WiFi.....
Connected!
1781131042,29.35,63.00
Calling: http://192.168.1.5:5000/predict?timestamp=...
HTTP Code: 200
Predicted next temp: 29.12°C
---

## 📈 Model Performance

| Metric | Value |
|---|---|
| Algorithm | Linear Regression |
| Training data | 18 real weather readings |
| Mean Absolute Error | 0.19°C |

> Note: Accuracy improves significantly with more data points collected 
> over longer periods.

---

## 🔮 Future Improvements

- Add DHT11 sensor for local real-time readings instead of API data
- Display predictions on OLED screen
- Collect data over weeks for better model accuracy
- Deploy Flask API to cloud (Render/Railway) for remote access
- Add more features (wind speed, pressure) to improve predictions
- Try LSTM model for time-series forecasting

---

## 👩‍💻 Author

**Apoorva R**
B.Tech ECE — VIT Vellore (2024–2028)

[LinkedIn](https://www.linkedin.com/in/apoorva-rr) | [GitHub](https://github.com/apoosharma)
