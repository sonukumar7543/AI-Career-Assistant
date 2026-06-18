from src.explainable_job_recommender import (
    recommend_jobs_explainable
)

resume_skills = [
    "Python",
    "Machine Learning",
    "Deep Learning"
]

results = recommend_jobs_explainable(
    resume_skills
)

for job in results:

    print("\n")
    print(job)