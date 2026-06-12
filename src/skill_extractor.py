# List of skills we want to detect
SKILLS = [
    "Python",
    "SQL",
    "Machine Learning",
    "Deep Learning",
    "TensorFlow",
    "PyTorch",
    "NLP",
    "Java",
    "C++",
    "JavaScript",
    "React",
    "Node.js"
]

def extract_skills(text):
    """
    Extract skills from resume text.
    """

    found_skills = []

    text_lower = text.lower()

    for skill in SKILLS:

        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills

