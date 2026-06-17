from src.ai_scorer import (
    calculate_ai_score
)

resume_skills = [
    "Python",
    "SQL",
    "Deep Learning"
]

job_skills = [
    "Python",
    "Neural Networks",
    "TensorFlow"
]

resume_text = """
Python SQL Deep Learning
"""

job_text = """
Python Neural Networks TensorFlow
"""

result = calculate_ai_score(
    resume_skills,
    job_skills,
    resume_text,
    job_text
)

print(result)