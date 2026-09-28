import json
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, ListItem, ListFlowable
from reportlab.platypus.flowables import HRFlowable, KeepTogether

# ===== CONFIGURATION =====
# Automatically get the script folder
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Input and Output paths
INPUT_JSON_FILE = os.path.join(SCRIPT_DIR, "..", "json", "resume.json")  # Path to your resume JSON file
OUTPUT_DIRECTORY = os.path.join(SCRIPT_DIR, "..", "pdf")  # Directory where PDF will be saved
OUTPUT_FILENAME = "Generated_CV.pdf"  # Name of the output PDF file

# Style Configuration - Customizable
ADD_HEADER_LINES = True  # Set to False to remove section header lines
PRIMARY_COLOR = colors.HexColor(0x004080)  # Dark blue color as seen in your example
SECTION_LINE_WIDTH = 0.5  # Thickness of section separator lines

# Font Sizes and Colors
TITLE_FONT_SIZE = 30  # Your name at the top
TITLE_FONT_COLOR = colors.HexColor(0x004080)  # Dark blue

HEADER_FONT_SIZE = 16  # Section headers (EDUCATION, EXPERIENCE, etc.)
HEADER_FONT_COLOR = colors.HexColor(0x004080)  # Dark blue

SUBHEADER_FONT_SIZE = 12  # Main entries (Ph.D., M.S., job titles, etc.)
SUBHEADER_FONT_COLOR = colors.black

INFO_FONT_SIZE = 10  # Regular text
INFO_FONT_COLOR = colors.black

DATE_FONT_SIZE = 10  # Dates
DATE_FONT_COLOR = colors.black

LOCATION_FONT_SIZE = 10  # Locations
LOCATION_FONT_COLOR = colors.black

# Contact Information (manually defined since not in JSON)
CONTACT_EMAIL = "ppuangch@purdue.edu"
CONTACT_PHONE = "+1 530 601 3173"
CONTACT_LINKEDIN = "Pattawee"
CONTACT_GITHUB = "Pattawee"
CONTACT_WEBSITE = "Pattawee.com"
# ===== END CONFIGURATION =====

def create_cv_pdf(json_file, output_path):
    """Create a PDF CV from JSON data"""
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Load the JSON data
    with open(json_file, 'r', encoding='utf-8') as f:
        cv_data = json.load(f)
    
    # Create the PDF document
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )
    
    # Define styles
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name='CVName',
        fontName='Helvetica-Bold',
        fontSize=TITLE_FONT_SIZE,
        leading=TITLE_FONT_SIZE+6,
        alignment=1,  # Center alignment
        textColor=TITLE_FONT_COLOR
    ))
    styles.add(ParagraphStyle(
        name='CVContact',
        fontName='Helvetica',
        fontSize=INFO_FONT_SIZE,
        leading=INFO_FONT_SIZE+2,
        alignment=1,  # Center alignment
        textColor=PRIMARY_COLOR
    ))
    styles.add(ParagraphStyle(
        name='CVSectionHeader',
        fontName='Helvetica-Bold',
        fontSize=HEADER_FONT_SIZE,
        leading=HEADER_FONT_SIZE+4,
        spaceBefore=12,
        spaceAfter=6,
        textColor=HEADER_FONT_COLOR,
        alignment=0  # Left alignment (0) for headers
    ))
    styles.add(ParagraphStyle(
        name='CVJobTitle',
        fontName='Helvetica-Bold',
        fontSize=SUBHEADER_FONT_SIZE,
        leading=SUBHEADER_FONT_SIZE+2,
        textColor=SUBHEADER_FONT_COLOR
    ))
    styles.add(ParagraphStyle(
        name='CVJobDetails',
        fontName='Helvetica-Oblique',
        fontSize=INFO_FONT_SIZE,
        leading=INFO_FONT_SIZE+2,
        textColor=INFO_FONT_COLOR
    ))
    styles.add(ParagraphStyle(
        name='CVNormal',
        fontName='Helvetica',
        fontSize=INFO_FONT_SIZE,
        leading=INFO_FONT_SIZE+2,
        textColor=INFO_FONT_COLOR
    ))
    styles.add(ParagraphStyle(
        name='CVDate',
        fontName='Helvetica',
        fontSize=DATE_FONT_SIZE,
        leading=DATE_FONT_SIZE+2,
        textColor=DATE_FONT_COLOR
    ))
    styles.add(ParagraphStyle(
        name='CVLocation',
        fontName='Helvetica',
        fontSize=LOCATION_FONT_SIZE,
        leading=LOCATION_FONT_SIZE+2,
        textColor=LOCATION_FONT_COLOR
    ))
    
    # Build content for the PDF
    content = []
    
    # Header with name and contact info
    basics = cv_data.get('basics', {})
    name = basics.get('Name', '')
    content.append(Paragraph(name, styles['CVName']))
    
    # Contact information
    content.append(Paragraph("Center for Global Trade Analysis, Department of Agricultural Economics, Purdue University", styles['CVContact']))
    content.append(Paragraph("KRAN #634 West Lafayette, IN 47907-2056 United States", styles['CVContact']))
    
    # Contact details line with proper icons
    email_icon = "&#9993;" # Envelope
    phone_icon = "&#9742;" # Phone
    linkedin_icon = "in"
    github_icon = "G"
    web_icon = "&#128279;" # Chain link
    
    contact_line = f"{email_icon} {CONTACT_EMAIL} | {phone_icon} {CONTACT_PHONE} | {linkedin_icon} {CONTACT_LINKEDIN} | {github_icon} {CONTACT_GITHUB} | {web_icon} {CONTACT_WEBSITE}"
    content.append(Paragraph(contact_line, styles['CVContact']))
    
    content.append(Spacer(1, 0.3*inch))
    
    # Education section
    content.append(Paragraph("EDUCATION", styles['CVSectionHeader']))
    
    # Add section line if enabled in config
    if ADD_HEADER_LINES:
        content.append(HRFlowable(
            width="100%",
            thickness=SECTION_LINE_WIDTH,
            color=PRIMARY_COLOR,
            spaceAfter=0.1*inch
        ))
    
    for edu in cv_data.get('education', []):
        # Create a table for each education entry
        data = []
        
        # Degree and Institution
        degree = edu.get('studyType', '')
        institution = edu.get('institution', '')
        area = edu.get('area', '')
        
        # Dates
        dates = []
        if edu.get('startDate'):
            dates.append(edu['startDate'])
        if edu.get('endDate'):
            dates.append(edu['endDate'])
        date_range = " – ".join(dates) if dates else ""
        
        # For Ph.D. and Masters, include dissertation/thesis
        if degree == "Ph.D." or degree == "M.S.":
            data.append([
                Paragraph(f"<b>{degree}</b>", styles['CVJobTitle']),
                Paragraph(f"<b>{institution}</b>, {area}", styles['CVJobTitle']),
                Paragraph(date_range, styles['CVDate'])
            ])
            
            if "Ph.D." in degree:
                data.append([
                    "",
                    Paragraph("Dissertation: <i>Incorporating Non-tariff Measures to Dynamic CGE Model</i>", styles['CVJobDetails']),
                    ""
                ])
            elif "M.S." in degree:
                data.append([
                    "",
                    Paragraph("Thesis: <i>The Impact of the ASEAN Economic Community on Agricultural Trade</i>", styles['CVJobDetails']),
                    ""
                ])
        else:
            # For B.S., include summa cum laude
            data.append([
                Paragraph(f"<b>{degree}</b>", styles['CVJobTitle']),
                Paragraph(f"<b>{institution}</b>, {area}, <i>summa cum laude</i>", styles['CVJobTitle']),
                Paragraph(date_range, styles['CVDate'])
            ])
        
        # Create and add the table
        table = Table(data, colWidths=[0.7*inch, 5.05*inch, 1.5*inch])
        table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 2),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ]))
        
        content.append(table)
        content.append(Spacer(1, 0.1*inch))
    
    # Experience section
    content.append(Spacer(1, 0.2*inch))
    content.append(Paragraph("EXPERIENCE", styles['CVSectionHeader']))
    
    # Add section line if enabled in config
    if ADD_HEADER_LINES:
        content.append(HRFlowable(
            width="100%",
            thickness=SECTION_LINE_WIDTH,
            color=PRIMARY_COLOR,
            spaceAfter=0.1*inch
        ))
    
    for job in cv_data.get('work', []):
        # Create a table for each job entry
        data = []
        
        # Position and Company
        position = job.get('position', '')
        company = job.get('name', '')
        location = job.get('location', '')
        
        # Dates
        dates = []
        if job.get('startDate'):
            dates.append(job['startDate'])
        if job.get('endDate'):
            dates.append(job['endDate'])
        date_range = " – ".join(dates) if dates else ""
        
        data.append([
            Paragraph(f"{location}<br/>{date_range}", styles['CVLocation']),
            Paragraph(f"<b>{position}</b>, {company}", styles['CVJobTitle'])
        ])
        
        # Add summary if any
        if job.get('summary'):
            data.append([
                "",
                Paragraph(job['summary'], styles['CVNormal'])
            ])
        
        # Add highlights as bullet points
        if job.get('highlights'):
            bullets = []
            for highlight in job.get('highlights', []):
                bullets.append(ListItem(Paragraph(f"<i>{highlight}</i>" if highlight.startswith("Focused on:") else highlight, 
                                                 styles['CVNormal'])))
            
            if bullets:
                data.append([
                    "",
                    ListFlowable(bullets, bulletType='bullet', start='•', leftIndent=20)
                ])
        
        # Create and add the table
        table = Table(data, colWidths=[1.5*inch, 5.25*inch])
        table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 2),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ]))
        
        content.append(table)
        content.append(Spacer(1, 0.1*inch))
    
    # Add all other sections with the same pattern
    
    # Projects section
    if 'projects' in cv_data and cv_data.get('projects'):
        content.append(Spacer(1, 0.2*inch))
        content.append(Paragraph("PROJECTS", styles['CVSectionHeader']))
        
        # Add section line if enabled in config
        if ADD_HEADER_LINES:
            content.append(HRFlowable(
                width="100%",
                thickness=SECTION_LINE_WIDTH,
                color=PRIMARY_COLOR,
                spaceAfter=0.1*inch
            ))
        
        for project in cv_data.get('projects', []):
            # Create a table for each project entry
            data = []
            
            # Project name
            name = project.get('name', '')
            
            # Dates if available
            dates = []
            if project.get('startDate'):
                dates.append(project['startDate'])
            if project.get('endDate'):
                dates.append(project['endDate'])
            date_range = " – ".join(dates) if dates else ""
            
            data.append([
                Paragraph(date_range, styles['CVDate']) if date_range else "",
                Paragraph(f"<b>{name}</b>", styles['CVJobTitle'])
            ])
            
            # Add summary
            if project.get('summary'):
                data.append([
                    "",
                    Paragraph(project['summary'], styles['CVNormal'])
                ])
            
            # Add highlights as bullet points
            if project.get('highlights'):
                bullets = []
                for highlight in project.get('highlights', []):
                    bullets.append(ListItem(Paragraph(highlight, styles['CVNormal'])))
                
                if bullets:
                    data.append([
                        "",
                        ListFlowable(bullets, bulletType='bullet', start='•', leftIndent=20)
                    ])
            
            # Create and add the table
            table = Table(data, colWidths=[1.5*inch, 5.25*inch])
            table.setStyle(TableStyle([
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('TOPPADDING', (0, 0), (-1, -1), 2),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
            ]))
            
            content.append(table)
            content.append(Spacer(1, 0.1*inch))
    
    # Publications section
    if 'publications' in cv_data and cv_data.get('publications'):
        content.append(Spacer(1, 0.2*inch))
        content.append(Paragraph("PUBLICATIONS", styles['CVSectionHeader']))
        
        # Add section line if enabled in config
        if ADD_HEADER_LINES:
            content.append(HRFlowable(
                width="100%",
                thickness=SECTION_LINE_WIDTH,
                color=PRIMARY_COLOR,
                spaceAfter=0.1*inch
            ))
        
        for pub in cv_data.get('publications', []):
            # Create a table for each publication entry
            data = []
            
            # Publication name
            name = pub.get('name', '')
            
            # Publication info
            pub_info = []
            if pub.get('authors'):
                pub_info.append(pub['authors'])
            if pub.get('releaseDate'):
                pub_info.append(pub['releaseDate'])
            
            data.append([Paragraph(f"<b>{name}</b>", styles['CVJobTitle'])])
            
            if pub_info:
                data.append([Paragraph(", ".join(pub_info), styles['CVJobDetails'])])
            
            # Add summary if any
            if pub.get('summary'):
                data.append([Paragraph(pub['summary'], styles['CVNormal'])])
            
            # Create and add the table
            table = Table(data, colWidths=[6.75*inch])
            table.setStyle(TableStyle([
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('TOPPADDING', (0, 0), (-1, -1), 2),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
            ]))
            
            content.append(table)
            content.append(Spacer(1, 0.1*inch))
    
    # Skills section
    if 'skills' in cv_data and cv_data.get('skills'):
        content.append(Spacer(1, 0.2*inch))
        content.append(Paragraph("SKILLS", styles['CVSectionHeader']))
        
        # Add section line if enabled in config
        if ADD_HEADER_LINES:
            content.append(HRFlowable(
                width="100%",
                thickness=SECTION_LINE_WIDTH,
                color=PRIMARY_COLOR,
                spaceAfter=0.1*inch
            ))
        
        for skill_category in cv_data.get('skills', []):
            # Create a table for each skill category
            data = []
            
            # Add category name
            if skill_category.get('name'):
                data.append([Paragraph(f"<b>{skill_category['name']}:</b>", styles['CVJobTitle'])])
            
            # Add description if any
            if skill_category.get('description'):
                data.append([Paragraph(skill_category['description'], styles['CVNormal'])])
            
            # Add skill levels and keywords
            for level in skill_category.get('levels', []):
                if level.get('level'):
                    level_text = f"<b>{level['level']}:</b> "
                    keywords = level.get('keywords', [])
                    if keywords:
                        level_text += ", ".join(keywords)
                    
                    data.append([Paragraph(level_text, styles['CVNormal'])])
            
            # Create and add the table
            table = Table(data, colWidths=[6.75*inch])
            table.setStyle(TableStyle([
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('TOPPADDING', (0, 0), (-1, -1), 2),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
            ]))
            
            content.append(table)
            content.append(Spacer(1, 0.1*inch))
    
    # Awards section
    if 'awards' in cv_data and cv_data.get('awards'):
        content.append(Spacer(1, 0.2*inch))
        content.append(Paragraph("SCHOLARSHIP & AWARDS", styles['CVSectionHeader']))
        
        # Add section line if enabled in config
        if ADD_HEADER_LINES:
            content.append(HRFlowable(
                width="100%",
                thickness=SECTION_LINE_WIDTH,
                color=PRIMARY_COLOR,
                spaceAfter=0.1*inch
            ))
        
        for award in cv_data.get('awards', []):
            # Create a table for each award entry
            data = []
            
            # Award title and date
            title = award.get('title', '')
            date = award.get('date', '')
            
            data.append([
                Paragraph(date, styles['CVDate']) if date else "",
                Paragraph(f"<b>{title}</b>", styles['CVJobTitle'])
            ])
            
            # Add summary if any
            if award.get('summary'):
                data.append([
                    "",
                    Paragraph(award['summary'], styles['CVNormal'])
                ])
            
            # Create and add the table
            table = Table(data, colWidths=[1.5*inch, 5.25*inch])
            table.setStyle(TableStyle([
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('TOPPADDING', (0, 0), (-1, -1), 2),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
            ]))
            
            content.append(table)
            content.append(Spacer(1, 0.1*inch))
    
    # Volunteer/Leadership section
    if 'volunteer' in cv_data and cv_data.get('volunteer'):
        content.append(Spacer(1, 0.2*inch))
        content.append(Paragraph("LEADERSHIP AND SERVICE", styles['CVSectionHeader']))
        
        # Add section line if enabled in config
        if ADD_HEADER_LINES:
            content.append(HRFlowable(
                width="100%",
                thickness=SECTION_LINE_WIDTH,
                color=PRIMARY_COLOR,
                spaceAfter=0.1*inch
            ))
        
        for vol in cv_data.get('volunteer', []):
            # Create a table for each volunteer entry
            data = []
            
            # Position and Organization
            position = vol.get('position', '')
            organization = vol.get('organization', '')
            
            # Dates
            dates = []
            if vol.get('startDate'):
                dates.append(vol['startDate'])
            if vol.get('endDate'):
                dates.append(vol['endDate'])
            date_range = " – ".join(dates) if dates else ""
            
            data.append([
                Paragraph(date_range, styles['CVDate']) if date_range else "",
                Paragraph(f"<b>{position}</b>, {organization}", styles['CVJobTitle'])
            ])
            
            # Add summary if any
            if vol.get('summary'):
                data.append([
                    "",
                    Paragraph(vol['summary'], styles['CVNormal'])
                ])
            
            # Add highlights as bullet points
            if vol.get('highlights'):
                bullets = []
                for highlight in vol.get('highlights', []):
                    bullets.append(ListItem(Paragraph(highlight, styles['CVNormal'])))
                
                if bullets:
                    data.append([
                        "",
                        ListFlowable(bullets, bulletType='bullet', start='•', leftIndent=20)
                    ])
            
            # Create and add the table
            table = Table(data, colWidths=[1.5*inch, 5.25*inch])
            table.setStyle(TableStyle([
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('TOPPADDING', (0, 0), (-1, -1), 2),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
            ]))
            
            content.append(table)
            content.append(Spacer(1, 0.1*inch))
    
    # References section
    if 'references' in cv_data and cv_data.get('references'):
        content.append(Spacer(1, 0.2*inch))
        content.append(Paragraph("REFERENCES", styles['CVSectionHeader']))
        
        # Add section line if enabled in config
        if ADD_HEADER_LINES:
            content.append(HRFlowable(
                width="100%",
                thickness=SECTION_LINE_WIDTH,
                color=PRIMARY_COLOR,
                spaceAfter=0.1*inch
            ))
        
        # Create a two-column table for references
        ref_data = []
        refs = cv_data.get('references', [])
        
        # Process references in pairs
        for i in range(0, len(refs), 2):
            row = []
            
            # First reference in pair
            ref1 = refs[i]
            ref1_text = f"<b>{ref1.get('name', '')}</b><br/>{ref1.get('reference', '')}"
            row.append(Paragraph(ref1_text, styles['CVNormal']))
            
            # Second reference in pair (if exists)
            if i + 1 < len(refs):
                ref2 = refs[i + 1]
                ref2_text = f"<b>{ref2.get('name', '')}</b><br/>{ref2.get('reference', '')}"
                row.append(Paragraph(ref2_text, styles['CVNormal']))
            else:
                row.append("")
            
            ref_data.append(row)
        
        # Create and add the references table
        ref_table = Table(ref_data, colWidths=[3.375*inch, 3.375*inch])
        ref_table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 2),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ]))
        
        content.append(ref_table)
    
    # Build the PDF
    doc.build(content)
    
    return output_path

def generate_cv():
    """Main function to generate the CV PDF from JSON data"""
    # Construct the full output path
    output_pdf_path = os.path.join(OUTPUT_DIRECTORY, OUTPUT_FILENAME)
    
    try:
        # Generate PDF
        pdf_path = create_cv_pdf(INPUT_JSON_FILE, output_pdf_path)
        print(f"CV generated successfully at: {pdf_path}")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    generate_cv()