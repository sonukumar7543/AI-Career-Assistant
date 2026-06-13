from src.parser import parse_resume
from src.parser import extract_text

from src.section_parser import extract_sections

from src.education_extractor import extract_education
from src.project_extractor import extract_projects
from src.experience_extractor import extract_experience


def build_resume(pdf_path):
    #Build complete structured resume.

    # Basic information
    resume_data = parse_resume(pdf_path)

    # Full text
    text = extract_text(pdf_path)

    # Sections
    sections = extract_sections(text)

    # Structured sections
    education = extract_education(sections)
    project = extract_projects(sections)
    experience = extract_experience(sections)

    # Combine everything
    resume_data["education"] = education
    resume_data["project"] = project
    resume_data["experience"] = experience

    return resume_data