from src.job_database import JOB_DATABASE
from src.semantic_matcher import similarity_score


def recommend_jobs_explainable(
    resume_skills,
    threshold=0.70
):

    recommendations = []

    for job, job_skills in JOB_DATABASE.items():

        matched_skills = []
        missing_skills = []

        for job_skill in job_skills:

            found = False

            for resume_skill in resume_skills:

                score = similarity_score(
                    resume_skill,
                    job_skill
                )

                if score >= threshold:

                    matched_skills.append(
                        job_skill
                    )

                    found = True
                    break

            if not found:

                missing_skills.append(
                    job_skill
                )

        score = (
            len(matched_skills)
            /
            len(job_skills)
        ) * 100

        recommendations.append({

            "job": job,

            "score": round(
                score,
                2
            ),

            "matched_skills":
                matched_skills,

            "missing_skills":
                missing_skills
        })

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations