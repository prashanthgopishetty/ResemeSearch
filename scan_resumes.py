import os
import re
import pdfplumber
import docx
import pandas as pd
import spacy

# Load NLP model (download using: python -m spacy download en_core_web_sm)
nlp = spacy.load("en_core_web_sm")

RESUME_FOLDER = "/Users/prashantgopishetty/Downloads/resume"  # Change to your folder path

SKILLS = {"Python", "Java", "C++", "SQL", "AWS", "Azure", "Docker", "Kubernetes", "Machine Learning", "Data Science"}

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text  # Return the first detected name
    return "Not Found"

def extract_phone(text):
    phone_pattern = re.compile(r"\+?\d{1,2}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}")
    phones = phone_pattern.findall(text)
    return phones[0] if phones else "Not Found"

def extract_email(text):
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    emails = email_pattern.findall(text)
    return emails[0] if emails else "Not Found"

def extract_skills(text):
    text_words = set(text.lower().split())
    found_skills = {skill for skill in SKILLS if skill.lower() in text_words}
    return ", ".join(found_skills)

def extract_location(text):
    doc = nlp(text)
    locations = [ent.text for ent in doc.ents if ent.label_ == "GPE"]
    return ", ".join(set(locations)) if locations else "Not Found"

def process_resumes():
    data = []

    for filename in os.listdir(RESUME_FOLDER):
        if re.match(r"^[^a-zA-Z0-9]", filename):  # Ignore files that start with special characters
            continue

        file_path = os.path.join(RESUME_FOLDER, filename)

        if filename.endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        elif filename.endswith(".docx"):
            text = extract_text_from_docx(file_path)
        else:
            continue

        name = extract_name(text)
        phone = extract_phone(text)
        email = extract_email(text)
        skills = extract_skills(text)
        location = extract_location(text)

        data.append({"Filename": filename, "Name": name, "Phone": phone, "Email": email, "Skills": skills, "Location": location})

    df = pd.DataFrame(data)
    df.to_excel("Resume_Summary.xlsx", index=False)
    print("Excel file generated successfully!")

# Run the script
process_resumes()
