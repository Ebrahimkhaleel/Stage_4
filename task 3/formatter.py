def format_txt(resume):
    content = f"Resume\n\nName: {resume['name']}\nEmail: {resume['email']}\nPhone: {resume['phone']}\n\nEducation:\n"
    for edu in resume['education']:
        content += f"- {edu['degree']} at {edu['school']} ({edu['year']})\n"
    content += "\nExperience:\n"
    for exp in resume['experience']:
        content += f"- {exp['title']} at {exp['company']} ({exp['years']})\n"
    content += "\nSkills:\n"
    for skill in resume['skills']:
        content += f"- {skill}\n"
    return content

def format_md(resume):
    content = f"# Resume\n\n## {resume['name']}\n**Email**: {resume['email']}  \n**Phone**: {resume['phone']}\n\n## Education\n"
    for edu in resume['education']:
        content += f"- **{edu['degree']}**, {edu['school']} ({edu['year']})\n"
    content += "\n## Experience\n"
    for exp in resume['experience']:
        content += f"- **{exp['title']}**, {exp['company']} ({exp['years']})\n"
    content += "\n## Skills\n"
    for skill in resume['skills']:
        content += f"- {skill}\n"
    return content