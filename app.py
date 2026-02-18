from flask import Flask, render_template, request, jsonify
import os
import pickle
import numpy as np
import requests

app = Flask(__name__)

# ================= MODEL LOAD =================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "power_prediction.sav")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

WEATHER_API_KEY = "wheather api key"

# ================= ROUTES =================

@app.route("/")
def home():
    return render_template("intro.html")

@app.route("/prediction")
def prediction():
    return render_template("predict.html")

@app.route("/map")
def map_page():
    return render_template("map.html")

# ================= WEATHER =================

@app.route("/api/weather/<city>")
def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return jsonify({"error": data.get("message", "API error")})

    return jsonify({
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "wind_speed": data["wind"]["speed"],
        "wind_direction": data["wind"].get("deg", 0)
    })

# ================= PREDICT =================

@app.route("/api/predict", methods=["POST"])
def predict_energy():

    data = request.json

    features = np.array([[
        data["temperature"],
        data["humidity"],
        data["temperature"] - 5,
        data["wind_speed"],
        data["wind_speed"] * 1.2,
        data["wind_direction"],
        data["wind_direction"],
        data["wind_speed"] * 1.5
    ]])

    power = model.predict(features)[0]

    return jsonify({"power": round(power, 2)})

# ================= MAP CLICK =================

@app.route("/api/predict-location")
def predict_location():

    lat = request.args.get("lat")
    lon = request.args.get("lon")

    weather = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=metric"
    ).json()

    if "main" not in weather:
        return jsonify({"error": "Weather fetch failed"})

    temp = weather["main"]["temp"]
    humidity = weather["main"]["humidity"]
    pressure = weather["main"]["pressure"]
    wind_speed = weather["wind"]["speed"]
    wind_direction = weather["wind"].get("deg", 0)

    features = np.array([[
        temp,
        humidity,
        temp - 5,
        wind_speed,
        wind_speed * 1.2,
        wind_direction,
        wind_direction,
        wind_speed * 1.5
    ]])

    power = model.predict(features)[0]

    return jsonify({
        "latitude": lat,
        "longitude": lon,
        "temperature": temp,
        "humidity": humidity,
        "pressure": pressure,
        "wind_speed": wind_speed,
        "power": round(power, 2)
    })

if __name__ == "__main__":
    app.run(debug=True)
