# AI Career Assistant

## Week 1 Progress

### Features Implemented

- PDF Resume Parsing
- Name Extraction
- Email Extraction
- Phone Extraction
- Skill Extraction
- JSON Output Generation

### Example Output

```json
{
    "name": "John Doe",
    "email": "john.doe@gmail.com",
    "phone": "9876543210",
    "skills": [
        "Python",
        "SQL",
        "Machine Learning",
        "NLP"
    ]
}
```
## Week 2 Progress

- Resume Section Detection
- Education Extraction
- Project Extraction
- Experience Extraction
- Structured Resume Builder

### Example Output

```json
{
    "name": "John Doe",
    "email": "john.doe@gmail.com",
    "phone": "9876543210",
    "skills": [
        "Python",
        "SQL",
        "Machine Learning",
        "NLP"
    ],
    "education": {
        "degree": "B.Tech in Computer Science",
        "university": "XYZ University",
        "cgpa": "8.5"
    },
    "project": {
        "project_name": "AI Career Assistant",
        "description": [
            "Built a resume analysis system.",
            "Extracted skills from resumes using NLP.",
            "Compared resumes with job descriptions."
        ]
    },
    "experience": {
        "job_title": "Data Analyst Intern",
        "company": "ABC Company",
        "duration": "June 2025 - August 2025",
        "experience_type": "Internship"
    }
}
```


## Week 3 Progress

### Resume Scoring Engine

Compare resume skills against job requirements and calculate a match score.

Example:

```json
{
    "score": 60.0,
    "matched_skills": [
        "Python",
        "SQL",
        "Machine Learning"
    ],
    "missing_skills": [
        "TensorFlow",
        "PyTorch"
    ]
}
```

### Job Description Parsing

Extract required skills directly from job descriptions.

### Skill Gap Analysis

Identify missing skills needed for a target role.

### Learning Recommendations

Recommend learning resources based on missing skills.

Example:

* TensorFlow -> Official TensorFlow Tutorials
* PyTorch -> PyTorch Learn

### Report Generation

Generate a complete career analysis report containing:

* Resume Score
* Matched Skills
* Missing Skills
* Learning Recommendations

### Current Pipeline

Resume PDF
↓
Resume Parser
↓
Structured Resume
↓
Job Description Parser
↓
Resume Scorer
↓
Skill Gap Analysis
↓
Learning Recommendations
↓
Career Report
