# # Import parser function
# from src.parser import parse_resume

# # Import json module
# import json


# # Path of resume file
# pdf_path = "resumes/test_resume.pdf"

# # Parse resume
# resume_data = parse_resume(pdf_path)

# # Print extracted information
# print("\n===== Resume Information =====")
# print(resume_data)

# # Save output as JSON
# with open("outputs/resume.json", "w") as file:

#     json.dump(
#         resume_data,
#         file,
#         indent=4
#     )

# print("\nResume parsed successfully!")
# print("Output saved in outputs/resume.json")

from src.parser import extract_text
from src.section_parser import extract_sections
from src.education_extractor import extract_education

text = extract_text("resumes/test_resume.pdf")

sections = extract_sections(text)

education = extract_education(sections)

print(education)