# Import required libraries
import pdfplumber
import re
import spacy
from src.skill_extractor import extract_skills

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")


def extract_text(pdf_path):
    #Extracts all text from a PDF file.

    text = ""

    # Open PDF
    with pdfplumber.open(pdf_path) as pdf:

        # Loop through each page
        for page in pdf.pages:

            # Extract text from current page
            page_text = page.extract_text()

            # Check if page contains text
            if page_text:
                text += page_text + "\n"

    return text


#Extract email address from text.

def extract_email(text):

    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    emails = re.findall(email_pattern, text)

    return emails[0] if emails else None


#Extract 10-digit phone number.

def extract_phone(text):

    phone_pattern = r'\d{10}'

    phones = re.findall(phone_pattern, text)

    return phones[0] if phones else None


#Extract candidate name using spaCy NER.

def extract_name(text):
    # Extract candidate name from first line of resume.

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        # Skip empty lines
        if line:
            return line

    return None


def parse_resume(pdf_path):
    # Main function that parses resume and returns structured information.

    # Extract full text from PDF
    text = extract_text(pdf_path)

    # Create structured output
    resume_data = {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text)
    }

    return resume_data