from src.semantic_matcher import similarity_score


def resume_job_similarity(
    resume_text,
    job_text
):
    """
    Compare complete resume text
    with complete job description.
    """

    score = similarity_score(
        resume_text,
        job_text
    )

    return round(score * 100, 2)