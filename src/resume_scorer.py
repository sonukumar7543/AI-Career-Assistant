def score_resume(
    resume_skills,
    required_skills
):

   # Compare resume skills with job requirements.

    matched_skills = []

    missing_skills = []

    # Convert resume skills to lowercase
    normalized_resume_skills = [
        skill.lower()
        for skill in resume_skills
    ]

    for skill in required_skills:

        if skill.lower() in normalized_resume_skills:

            matched_skills.append(skill)

        else:

            missing_skills.append(skill)

    score = (
        len(matched_skills)
        / len(required_skills)
    ) * 100

    return {
        "score": round(score, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }