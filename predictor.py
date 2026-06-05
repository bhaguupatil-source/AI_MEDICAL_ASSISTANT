import joblib

model = joblib.load(
    "models/disease_model.pkl"
)

encoder = joblib.load(
    "models/encoder.pkl"
)

def predict_disease(symptoms):

    pred = model.predict([symptoms])

    disease = encoder.inverse_transform(pred)

    return disease[0]