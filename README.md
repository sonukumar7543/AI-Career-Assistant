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



# Week 4 - FastAPI Backend & Web Interface

## Overview

In Week 4, the AI Career Assistant was transformed from a command-line application into a web application using FastAPI and Jinja2 templates.

Users can now upload a resume, provide a job description, and receive an automated career analysis directly from a web browser.

---

## Features Implemented

### 1. FastAPI Backend

Created a FastAPI server to expose the project functionality through REST APIs.

Endpoints:

* `GET /`
* `POST /parse-resume`
* `POST /analyze-resume`

---

### 2. Resume Upload API

Users can upload a PDF resume.

The API:

* Saves the uploaded file
* Parses resume content
* Extracts structured information


### 3. Resume Analysis API

Users can submit:

* Resume PDF
* Job Description

The system:

* Extracts resume skills
* Extracts required job skills
* Calculates ATS-style score
* Identifies missing skills
* Generates learning recommendations


### 4. Pydantic Models

Implemented Pydantic response models for:

* Data validation
* Type checking
* Better API documentation


### 5. Jinja2 Templates

Added server-side rendered HTML pages.

### 6. Frontend Integration

Built a basic web interface where users can:

1. Upload Resume
2. Paste Job Description
3. Click Analyze Resume
4. View Analysis Results


### 7. Results Page

Displays:

* Candidate Name
* Resume Score
* Matched Skills
* Missing Skills
* Learning Recommendations

---

### 8. CSS Styling

Added custom styling using:

Improvements:

* Better spacing
* Improved readability
* Cleaner layout


## Current Architecture

```text
User
  ↓
Web Interface
  ↓
FastAPI Backend
  ↓
Resume Parser
  ↓
Job Description Parser
  ↓
Resume Scorer
  ↓
Recommendation Engine
  ↓
Results Page
```

---

## Technologies Used

* Python
* FastAPI
* Jinja2
* HTML
* CSS
* Pydantic
* spaCy
* PyPDF2

---
