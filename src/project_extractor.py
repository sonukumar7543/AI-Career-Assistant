def extract_projects(sections):

    # Extract project information from PROJECTS section.

    projects = sections.get("PROJECTS", [])

    if not projects:
        return None

    result = {
        "project_name": None,
        "description": []
    }

    # First line is usually project title
    result["project_name"] = projects[0]

    # Remaining lines are descriptions
    for line in projects[1:]:

        # Remove dashes if present
        clean_line = line.replace("-", "").strip()

        result["description"].append(clean_line)

    return result