import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "T1.csv")
MODEL_PATH = os.path.join(BASE_DIR, "power_prediction.sav")

df = pd.read_csv(DATA_PATH)

if "Time" in df.columns:
    df.drop("Time", axis=1, inplace=True)

df.dropna(inplace=True)

X = df.drop("Power", axis=1)
y = df["Power"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(n_estimators=300, random_state=42)
model.fit(X_train, y_train)

with open(MODEL_PATH, "wb") as f:
    pickle.dump(model, f)

print("Model trained successfully!")
