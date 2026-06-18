from src.job_recommender import (
    recommend_jobs
)

resume_skills = [
    "Python",
    "Machine Learning",
    "TensorFlow",
    "NLP"
]

results = recommend_jobs(
    resume_skills
)

for job in results:

    print(job)