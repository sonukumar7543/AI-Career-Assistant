from src.job_database import JOB_DATABASE


def recommend_jobs(
    resume_skills
):

    recommendations = []

    resume_skills = [
        skill.lower()
        for skill in resume_skills
    ]

    for job, skills in JOB_DATABASE.items():

        matched = 0

        for skill in skills:

            if skill.lower() in resume_skills:

                matched += 1

        score = (
            matched
            /
            len(skills)
        ) * 100

        recommendations.append(
            {
                "job": job,
                "score": round(score, 2)
            }
        )

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations