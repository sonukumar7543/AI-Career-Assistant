def extract_experience(sections):
    # Extract structured experience information.

    experience = sections.get("EXPERIENCE", [])

    if not experience:
        return None

    result = {
        "job_title": None,
        "company": None,
        "duration": None,
        "experience_type": None
    }

    # Job title is usually first line
    if len(experience) > 0:
        result["job_title"] = experience[0]

    # Company name is usually second line
    if len(experience) > 1:
        result["company"] = experience[1]

    # Duration is usually third line
    if len(experience) > 2:
        result["duration"] = experience[2]

    if result["job_title"]:
        title = result["job_title"].lower()
        if "intern" in title:
            result["experience_type"] = "Internship"

        elif "freelance" in title:
            result["experience_type"] = "Freelance"

        elif "contract" in title:
            result["experience_type"] = "Contract"

        else:
            result["experience_type"] = "Full Time"

        return result