from src.parser import extract_text

text = extract_text("resumes/test_resume.pdf")

print(repr(text))