from src.semantic_job_recommender import (
    recommend_jobs_semantic
)

resume_skills = [
    "Python",
    "Machine Learning",
    "Deep Learning"
]

results = recommend_jobs_semantic(
    resume_skills
)

for job in results:
    print(job)