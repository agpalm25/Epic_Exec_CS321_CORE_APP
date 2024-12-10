# utils.py
import fitz
import re

def extract_text_from_pdf(pdf_file):
    text = ""
    extracted_data = {
        "name": None,
        "email": None,
        "phone_number": None,
        "education": None,
        "experience": None,
        "skills": None,
        "certifications": None,
        "summary": None
    }

    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()

    # Extract Name (assume the first line of the resume is the name)
    lines = text.split('\n')
    if lines:
        extracted_data["name"] = lines[0].strip()

    # Extract Email
    email_match = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
    if email_match:
        extracted_data["email"] = email_match.group(0)

    # Extract Phone Number
    phone_match = re.search(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b', text)
    if phone_match:
        extracted_data["phone_number"] = phone_match.group(0)

    # Extract Education
    edu_section_start = text.find("Education")
    exp_section_start = text.find("Experience")
    if edu_section_start != -1 and exp_section_start != -1:
        extracted_data["education"] = text[edu_section_start:exp_section_start].strip()

    # Extract Skills
    skills_section_start = text.find("Technical Skills")
    if skills_section_start != -1:
        extracted_data["skills"] = text[skills_section_start:].strip()

    return extracted_data

