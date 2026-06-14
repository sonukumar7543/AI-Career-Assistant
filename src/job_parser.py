from src.skill_extractor import extract_skills


def parse_job_description(file_path):

    with open(file_path, "r") as file:

        text = file.read()

    skills = extract_skills(text)

    return {
        "text": text,
        "skills": skills
    }