from src.job_database import JOB_DATABASE
from src.semantic_matcher import similarity_score


def recommend_jobs_semantic(
    resume_skills,
    threshold=0.70
):

    recommendations = []

    for job, job_skills in JOB_DATABASE.items():

        matched = 0

        for job_skill in job_skills:

            found = False

            for resume_skill in resume_skills:

                score = similarity_score(
                    resume_skill,
                    job_skill
                )

                if score >= threshold:

                    matched += 1
                    found = True
                    break

            if found:
                continue

        score = (
            matched /
            len(job_skills)
        ) * 100

        recommendations.append({
            "job": job,
            "score": round(score, 2)
        })

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations