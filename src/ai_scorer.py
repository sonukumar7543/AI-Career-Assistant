from src.hybrid_scorer import hybrid_score
from src.document_similarity import (
    resume_job_similarity
)


def calculate_ai_score(
    resume_skills,
    job_skills,
    resume_text,
    job_text
):

    skill_result = hybrid_score(
        resume_skills,
        job_skills
    )

    semantic_score = (
        resume_job_similarity(
            resume_text,
            job_text
        )
    )

    final_score = (
        skill_result["score"] * 0.7
        +
        semantic_score * 0.3
    )

    return {
        "final_score":
            round(final_score, 2),

        "skill_score":
            skill_result["score"],

        "semantic_score":
            semantic_score,

        "matched_skills":
            skill_result["matched_skills"],

        "missing_skills":
            skill_result["missing_skills"]
    }