from src.semantic_scorer import semantic_match

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

result = semantic_match(
    resume_skills,
    job_skills
)

print(result)