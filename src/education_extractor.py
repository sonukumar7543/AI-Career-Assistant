def extract_education(sections):
    # Extract structured education information.

    education = sections.get("EDUCATION", [])

    result = {
        "degree": None,
        "university": None,
        "cgpa": None
    }

    for line in education:

        if "B.Tech" in line or "Bachelor" in line:
            result["degree"] = line

        elif "CGPA" in line:
            result["cgpa"] = line.replace("CGPA:", "").strip()

        else:
            if result["university"] is None:
                result["university"] = line

    return result