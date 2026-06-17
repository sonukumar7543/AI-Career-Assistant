from src.document_similarity import (
    resume_job_similarity
)

resume = """
Python
SQL
Deep Learning
NLP
"""

job = """
Machine Learning Engineer

Required Skills:

Python
TensorFlow
Neural Networks
NLP
"""

score = resume_job_similarity(
    resume,
    job
)

print(score)