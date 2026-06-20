import joblib
import numpy as np

model = joblib.load("models/career_model.pkl")

tfidf = joblib.load("models/career_tfidf.pkl")

encoder = joblib.load("models/career_encoder.pkl")


def predict_top_careers(skills):

    text = " ".join(skills)

    vector = tfidf.transform([text])

    scores = model.decision_function(vector)[0]

    top_indices = scores.argsort()[-3:][::-1]

    careers = []

    for idx in top_indices:

        careers.append(
            encoder.inverse_transform([idx])[0]
        )

    return careers