from src.hybrid_scorer import hybrid_score

resume_skills = [
    "Python",
    "SQL",
    "Deep Learning"
]

job_skills = [
    "Python",
    "Neural Networks",
    "TensorFlow"
]

result = hybrid_score(
    resume_skills,
    job_skills
)

print(result)