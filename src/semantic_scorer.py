from src.semantic_matcher import similarity_score


def semantic_match(
    resume_skills,
    job_skills,
    threshold=0.70
):

    matched = []

    missing = []

    for job_skill in job_skills:

        found = False

        for resume_skill in resume_skills:

            score = similarity_score(
                resume_skill,
                job_skill
            )

            if score >= threshold:

                matched.append(job_skill)

                found = True

                break

        if not found:

            missing.append(job_skill)

    return {
        "matched_skills": matched,
        "missing_skills": missing
    }