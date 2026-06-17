from src.semantic_matcher import similarity_score


def hybrid_score(
    resume_skills,
    required_skills,
    threshold=0.70
):

    matched_skills = []

    missing_skills = []

    for required_skill in required_skills:

        found = False

        for resume_skill in resume_skills:

            # Exact Match
            if (
                resume_skill.lower()
                ==
                required_skill.lower()
            ):

                matched_skills.append(
                    required_skill
                )

                found = True

                break

            # Semantic Match
            score = similarity_score(
                resume_skill,
                required_skill
            )

            if score >= threshold:

                matched_skills.append(
                    required_skill
                )

                found = True

                break

        if not found:

            missing_skills.append(
                required_skill
            )

    if len(required_skills) == 0:

        return {
            "score": 0,
            "matched_skills": [],
            "missing_skills": []
        }

    score = (
        len(matched_skills)
        /
        len(required_skills)
    ) * 100

    return {
        "score": round(score, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }