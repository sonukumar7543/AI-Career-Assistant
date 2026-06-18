import joblib


model = joblib.load("models/career_model.pkl")

tfidf = joblib.load("models/career_tfidf.pkl")

encoder = joblib.load("models/career_encoder.pkl")


def predict_career(
    skills
):

    text = " ".join(skills)

    vector = tfidf.transform(
        [text]
    )

    prediction = model.predict(
        vector
    )

    career = encoder.inverse_transform(
        prediction
    )

    return career[0]