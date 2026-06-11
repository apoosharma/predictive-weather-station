from flask import Flask, request, jsonify
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import pickle

# Train model
df = pd.read_csv('weather_data.csv', header=None, names=['timestamp', 'temp', 'humidity'])
df['next_temp'] = df['temp'].shift(-1)
df = df.dropna()

X = df[['timestamp', 'temp', 'humidity']]
y = df['next_temp']

model = LinearRegression()
model.fit(X, y)

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    timestamp = float(request.args.get('timestamp'))
    temp = float(request.args.get('temp'))
    humidity = float(request.args.get('humidity'))
    
    prediction = model.predict([[timestamp, temp, humidity]])
    return jsonify({'predicted_temp': round(float(prediction[0]), 2)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)