import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("data/disease_dataset.csv")

print(df.head())

X = df.drop("disease", axis=1)
y = df["disease"]

encoder = LabelEncoder()

y_encoded = encoder.fit_transform(y)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y_encoded)

joblib.dump(
    model,
    "models/disease_model.pkl"
)

joblib.dump(
    encoder,
    "models/encoder.pkl"
)

print("Model Saved")
