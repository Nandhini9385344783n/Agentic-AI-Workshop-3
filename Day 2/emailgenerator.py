def generate_resume(personal_info, experiences, education_entries, skills=""):
    """
    Generates a professionally formatted resume from provided data.

    Args:
        personal_info (dict): A dictionary containing personal details
                              (e.g., 'fullName', 'phone', 'email', 'linkedin', 'location', 'summary').
        experiences (list): A list of dictionaries, where each dictionary represents
                            a work experience with keys like 'jobTitle', 'companyName',
                            'jobLocation', 'startDate', 'endDate', 'responsibilities'.
        education_entries (list): A list of dictionaries, where each dictionary represents
                                  an education entry with keys like 'degree', 'major',
                                  'institution', 'gradDate'.
        skills (str): A comma-separated string of skills.

    Returns:
        str: A formatted string representing the resume.
    """
    resume_lines = []

    # --- Personal Information ---
    resume_lines.append(personal_info.get('fullName', '').upper())
    contact_info = []
    if personal_info.get('phone'):
        contact_info.append(personal_info['phone'])
    if personal_info.get('email'):
        contact_info.append(personal_info['email'])
    if personal_info.get('linkedin'):
        contact_info.append(personal_info['linkedin'])
    if personal_info.get('location'):
        contact_info.append(personal_info['location'])

    if contact_info:
        resume_lines.append(" | ".join(contact_info))
    resume_lines.append("-" * 50) # Separator for readability

    # --- Professional Summary ---
    if personal_info.get('summary'):
        resume_lines.append("\nPROFESSIONAL SUMMARY")
        resume_lines.append("-" * 20)
        resume_lines.append(personal_info['summary'])

    # --- Work Experience ---
    if experiences:
        resume_lines.append("\nWORK EXPERIENCE")
        resume_lines.append("-" * 17)
        for exp in experiences:
            title = exp.get('jobTitle', 'N/A')
            company = exp.get('companyName', 'N/A')
            location = exp.get('jobLocation', '')
            start_date = exp.get('startDate', '')
            end_date = exp.get('endDate', '')
            responsibilities = exp.get('responsibilities', '')

            resume_lines.append(f"**{title}** at {company}, {location}")
            resume_lines.append(f"{start_date} – {end_date}")
            if responsibilities:
                # Split responsibilities by newline and format as bullet points
                for resp_line in responsibilities.split('\n'):
                    if resp_line.strip(): # Ensure line is not empty
                        resume_lines.append(f"• {resp_line.strip()}")
            resume_lines.append("") # Add a blank line for separation

    # --- Education ---
    if education_entries:
        resume_lines.append("\nEDUCATION")
        resume_lines.append("-" * 9)
        for edu in education_entries:
            degree = edu.get('degree', 'N/A')
            major = edu.get('major', '')
            institution = edu.get('institution', 'N/A')
            grad_date = edu.get('gradDate', '')

            edu_line = f"**{degree}**"
            if major:
                edu_line += f", {major}"
            edu_line += f" from {institution}"
            resume_lines.append(edu_line)
            if grad_date:
                resume_lines.append(f"Graduated: {grad_date}")
            resume_lines.append("") # Add a blank line for separation

    # --- Skills ---
    if skills:
        resume_lines.append("\nSKILLS")
        resume_lines.append("-" * 6)
        # Simply list skills as provided, you might want to categorize them here
        resume_lines.append(skills)

    return "\n".join(resume_lines)

# Example Usage based on your provided data and the form structure:
personal_info_data = {
    'fullName': 'Nandhini',
    'phone': '98745126320',
    'email': 'nandhini@gmail.com',
    'linkedin': 'linkedin/nandhini',
    'location': 'Coimbatore, India',
    'summary': '' # Can be filled in later or generated by a model
}

experience_data = [
    {
        'jobTitle': 'Academic Coordinator',
        'companyName': 'SNS',
        'jobLocation': 'Coimbatore',
        'startDate': 'May, 20XX', # Assuming a start year, please update
        'endDate': 'Present',
        'responsibilities': '- Coordinated academic programs and activities.\n- Managed student records and scheduling.\n- Supported faculty in curriculum development.'
    }
]

education_data = [
    {
        'degree': 'Post Graduation',
        'major': '', # Add major if available
        'institution': '', # Add institution name
        'gradDate': '' # Add graduation date
    }
]

skills_data = 'Curriculum Development, Program Management, Student Support, Communication, Leadership' # Example skills

# Generate the resume
generated_resume = generate_resume(personal_info_data, experience_data, education_data, skills_data)
print(generated_resume)
