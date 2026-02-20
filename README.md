# 🌬 Weather-Based Prediction of Wind Turbine Energy Output  
### A Next-Generation Approach to Renewable Energy Management

---

## 📌 Project Overview

This project predicts the energy output of a wind turbine based on real-time weather conditions using Machine Learning.

Wind energy production depends heavily on dynamic atmospheric conditions such as:

- Temperature
- Humidity
- Wind Speed
- Wind Direction
- Derived wind parameters

By analyzing historical wind turbine datasets and training regression models, this system estimates turbine power generation for any city using live weather data from the OpenWeatherMap API.

This solution helps:

- ⚡ Energy production forecasting  
- 🛠 Maintenance planning  
- 🌍 Grid balancing  
- 📊 Renewable energy optimization  


## 📂 Project Structure

```
WindEnergyProject/
│
├── app.py                        # Flask backend
├── train_model.py                # Model training script
├── cluster_zones.py              # K-Means energy zone clustering
├── power_prediction.sav          # Trained ML model
├── requirements.txt              # Project dependencies
│
├── data/
│   └── T1.csv                    # Wind turbine dataset
│
├── templates/
│   ├── intro.html                # Landing page
│   ├── predict.html              # Weather + Prediction page
│   └── map.html                  # Map-based prediction
│
├── static/
│   ├── css/
│   │   └── style.css             # Styling
│   ├── js/
│   │   ├── predict.js            # Prediction logic
│   │   └── map.js                # Map interaction
│   └── images/
│       └── windmill.jpg          # Background image
│
└── Wind_mill_model.ipynb         # Jupyter notebook (ML experimentation)
```


## 🧠 Machine Learning Model

The project uses:

- **Random Forest Regressor**
- Trained on historical wind turbine dataset
- Evaluated using:
  - R² Score
  - MAE
  - RMSE

The trained model is serialized into:


The Flask app loads this model for real-time prediction.

---

## 🛠 Technologies Used

| Category | Technology |
|-----------|------------|
| Language | Python |
| ML Libraries | NumPy, Pandas, Scikit-learn |
| Visualization | Matplotlib, Seaborn |
| Model | Random Forest Regressor |
| Web Framework | Flask |
| API | OpenWeatherMap API |
| Frontend | HTML, CSS, JavaScript |
| Model Serialization | Pickle / Joblib |
| Development Tools | Jupyter Notebook, VS Code |

## document Link and Demo Video
link: https://drive.google.com/drive/folders/1qbc7kIPYLaBTwlPuHecv9_0gZeoMfAR7





