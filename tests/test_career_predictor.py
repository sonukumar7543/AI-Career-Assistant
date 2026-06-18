from src.career_predictor import predict_career


skills = [
    "Python",
    "TensorFlow",
    "Deep Learning",
    "NLP"
]

career = predict_career(
    skills
)

print(career)