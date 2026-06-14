import os
import json

from src.resume_builder import build_resume
from src.resume_scorer import score_resume
from src.job_parser import parse_job_description
from src.recommender import recommend_skills
from src.report_generator import generate_report


def main():
    """
    Main entry point of AI Career Assistant.
    """

    # Create outputs folder if it doesn't exist
    os.makedirs("outputs", exist_ok=True)

    # Parse Resume
    resume = build_resume(
        "resumes/test_resume.pdf"
    )

    # Parse Job Description
    job = parse_job_description(
        "job_descriptions/ml_engineer.txt"
    )

    # Score Resume
    result = score_resume(
        resume["skills"],
        job["skills"]
    )

    # Generate Recommendations
    recommendations = recommend_skills(
        result["missing_skills"]
    )

    # Generate Report
    report = generate_report(
        resume,
        result,
        recommendations
    )

    # Display Report
    print(report)

    # Save Structured Resume
    with open(
        "outputs/resume.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            resume,
            file,
            indent=4
        )

    # Save Report
    with open(
        "outputs/report.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(report)

    print("\nResume JSON saved!")
    print("Report saved!")


if __name__ == "__main__":
    main()