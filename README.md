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