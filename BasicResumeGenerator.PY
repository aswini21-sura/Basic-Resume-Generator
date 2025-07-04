import os
os.system("pip install fpdf")
from fpdf import FPDF # type: ignore
print("fpdf is working!")
import datetime

def get_user_data():
    print("\n--- Resume Generator ---\n")
    name = input("Enter your full name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")
    objective = input("Enter your career objective: ")
    education = input("Enter your education details: ")
    skills = input("Enter your technical skills (comma-separated): ")
    projects = input("Enter your project titles: ")
    internship = input("Enter your internships/summer training: ")
    experience = input("Enter your work experience (if any): ")
    certifications = input("Enter your certifications: ")
    achievements = input("Enter your achievements: ")
    strengths = input("Enter your strengths: ")
    hobbies = input("Enter your hobbies: ")
    declaration = input("Enter your declaration statement: ")
    
    return {
        "name": name,
        "email": email,
        "phone": phone,
        "address": address,
        "objective": objective,
        "education": education,
        "skills": skills,
        "projects": projects,
        "internship": internship,
        "experience": experience,
        "certifications": certifications,
        "achievements": achievements,
        "strengths": strengths,
        "hobbies": hobbies,
        "declaration": declaration,
        "date": datetime.datetime.now().strftime("%d-%m-%Y")
    }

def generate_resume_txt(data):
    with open("resume.txt", "w") as file:
        file.write(f"{'-'*30}\n")
        file.write(f"{' '*10}RESUME\n")
        file.write(f"{'-'*30}\n")
        file.write(f"Name: {data['name']}\n")
        file.write(f"Email: {data['email']}\n")
        file.write(f"Phone: {data['phone']}\n")
        file.write(f"Address: {data['address']}\n\n")
        file.write(f"Career Objective:\n{data['objective']}\n\n")
        file.write(f"Education:\n{data['education']}\n\n")
        file.write(f"Technical Skills:\n{data['skills']}\n\n")
        file.write(f"Projects:\n{data['projects']}\n\n")
        file.write(f"Internship:\n{data['internship']}\n\n")
        file.write(f"Experience:\n{data['experience']}\n\n")
        file.write(f"Certifications:\n{data['certifications']}\n\n")
        file.write(f"Achievements:\n{data['achievements']}\n\n")
        file.write(f"Strengths:\n{data['strengths']}\n\n")
        file.write(f"Hobbies:\n{data['hobbies']}\n\n")
        file.write(f"Declaration:\n{data['declaration']}\n")
        file.write(f"Date: {data['date']}\n")
        file.write(f"{'-'*30}\n")
    print("✅ Resume saved as 'resume.txt'")

def generate_resume_pdf(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="RESUME", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 10, f"Name: {data['name']}")
    pdf.multi_cell(0, 10, f"Email: {data['email']}")
    pdf.multi_cell(0, 10, f"Phone: {data['phone']}")
    pdf.multi_cell(0, 10, f"Address: {data['address']}")
    pdf.ln(5)

    pdf.set_font("Arial", 'B', size=11)
    pdf.cell(0, 10, "Career Objective:", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 10, data['objective'])
    
    pdf.set_font("Arial", 'B', size=11)
    pdf.cell(0, 10, "Education:", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 10, data['education'])

    pdf.set_font("Arial", 'B', size=11)
    pdf.cell(0, 10, "Technical Skills:", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 10, data['skills'])

    pdf.set_font("Arial", 'B', size=11)
    pdf.cell(0, 10, "Projects:", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 10, data['projects'])

    pdf.set_font("Arial", 'B', size=11)
    pdf.cell(0, 10, "Internship:", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 10, data['internship'])

    pdf.set_font("Arial", 'B', size=11)
    pdf.cell(0, 10, "Experience:", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 10, data['experience'])

    pdf.set_font("Arial", 'B', size=11)
    pdf.cell(0, 10, "Certifications:", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 10, data['certifications'])

    pdf.set_font("Arial", 'B', size=11)
    pdf.cell(0, 10, "Achievements:", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 10, data['achievements'])

    pdf.set_font("Arial", 'B', size=11)
    pdf.cell(0, 10, "Strengths:", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 10, data['strengths'])

    pdf.set_font("Arial", 'B', size=11)
    pdf.cell(0, 10, "Hobbies:", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 10, data['hobbies'])

    pdf.set_font("Arial", 'B', size=11)
    pdf.cell(0, 10, "Declaration:", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 10, data['declaration'])

    pdf.ln(5)
    pdf.cell(0, 10, f"Date: {data['date']}", ln=True)

    pdf.output("resume.pdf")
    print("✅ Resume saved as 'resume.pdf'")

# --- Run the Generator ---
user_data = get_user_data()
generate_resume_txt(user_data)
generate_resume_pdf(user_data)
