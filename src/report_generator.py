def generate_report(
    resume,
    score_result,
    recommendations
):
    # Generate formatted report.
    
    report = []

    report.append("=" * 40)
    report.append("AI CAREER ASSISTANT REPORT")
    report.append("=" * 40)

    report.append("")
    report.append(
        f"Candidate: {resume['name']}"
    )

    report.append("")
    report.append(
        f"Resume Score: {score_result['score']}%"
    )

    report.append("")
    report.append("Matched Skills:")

    for skill in score_result["matched_skills"]:
        report.append(f"✓ {skill}")

    report.append("")
    report.append("Missing Skills:")

    for skill in score_result["missing_skills"]:
        report.append(f"✗ {skill}")

    report.append("")
    report.append(
        "Learning Recommendations:"
    )

    for skill, info in recommendations.items():

        report.append("")
        report.append(skill)

        report.append(
            f"- Difficulty: {info['difficulty']}"
        )

        report.append(
            f"- Resource: {info['resource']}"
        )

    return "\n".join(report)