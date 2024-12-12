import smtplib
import os
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_email(to_email, subject, body):
    sender_email = os.environ.get('SENDER_EMAIL')
    sender_password = os.environ.get('SENDER_PASSWORD')
   
    if not sender_email or not sender_password:
        logger.error("SENDER_EMAIL or SENDER_PASSWORD environment variables are not set")
        raise ValueError("Email credentials are not properly configured")

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
   
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
        logger.info(f"Email sent successfully to {to_email}")
        return True
    except Exception as e:
        logger.error(f"Failed to send email to {to_email}. Error: {str(e)}")
        raise

def send_application_confirmation_email(applicant_email):
    subject = "CA Application Received - Thank You!"
    body = """
    Greetings,

    Thank you for submitting your application for the 2024/2025 Hall Staff Team. We are incredibly excited about your candidacy. To give you a heads-up on what our next steps are please see the below information.

    If you have not signed up for an interview, please do so at your earliest convenience.

    For returning CAs, interviews will be held in Page Balcony. These interviews will be held between March 5th and March 8th.

    For new CA candidates, interviews will be held in Diamond. More information regarding which specific room will be coming in the coming days. These interviews will be conducted on March 9th and March 10th.

    If you have any questions, please do not hesitate to contact us!

    Cheers,
    --
    Kyle Arthenayake M.Ed.
    Associate Director of Residential Education
    Colby's Office of the Residential Experience (CORE)
    """
   
    return send_email(applicant_email, subject, body)

def send_interview_confirmation_email(applicant_email, full_name, date, time):
    subject = "CA Interview Scheduled - Confirmation"
    body = f"""
    Dear {full_name},

    This email is to confirm that your CA interview has been scheduled for:

    Date: {date}
    Time: {time}

    For returning CAs, interviews will be held in Page Balcony.
    For new CA candidates, interviews will be held in Diamond. More specific room information will be provided soon.

    If you need to reschedule or have any questions, please contact us as soon as possible.

    We look forward to meeting with you!

    Best regards,
    Colby's Office of the Residential Experience (CORE)
    """
   
    return send_email(applicant_email, subject, body)

def send_assessment_result_email(applicant_email, preferred_name, last_name, student_id, result):
    if result == "Accepted":
        subject = "CA Offer Letter"
        body = f"""
        {preferred_name} {last_name}
        {student_id}

        Dear {preferred_name},

        Congratulations! The Office of Campus Life is pleased to offer you a Community Advisor position for the 2025-2026 academic year. On behalf of the Office, we are truly excited to welcome you to our team!

        The Community Advisor position is specifically designated as a full academic year position. The position responsibilities and expectations are described in the position description and the 2025-2026 Community Advisor Position Agreement. The period of employment begins as early as TBD, and ends TBD. The employment period includes training, and break closings/openings.

        If accepting the position, you will be given your placement, and your supervising ARD no later than TBD. 

        Please understand that this is a conditional position offer. Your offer and employment for the upcoming academic year is contingent upon the successful completion of the following:
        Maintaining a minimum 2.50 cumulative grade point average (GPA) - GPAs will be checked at the conclusion of each semester. If you do not meet the GPA requirement, you will be notified; and
        Remain in good student conduct standing with the College.

        In order to accept this offer, please complete the following:
        Review the 2025-2026 Community Advisor Position Agreement. This agreement outlines position obligations and responsibilities, important dates, and sets forth employment guidelines; 
        Electronically accept or decline the offered position by no later than TBD.

        If accepting the position, please officially apply through Workday. This application does not have any determination on your hireability as we have already gone through a hiring process. This form instead helps process and prepare for your employment.
        In Workday, Search for "Find Student Jobs" and click on Find Student Jobs – CR (report).
        Scroll through the jobs and review job descriptions which can also be found in the job book. It's helpful to search for Community Advisor or by "R0003473."
        Apply by clicking on the Apply button and uploading a resume and cover letter to express your interest.

        Save the Date - August Training: Per the 2025-2026 Community Advisor Position Agreement, you are required to attend Fall Hall Staff Training beginning as early as TBD. Training and move-in preparations will continue through the first day of classes. Please use these dates for planning purposes. 

        Please Note: Employment timeframes are aligned with the Colby College Academic Calendar but may require flexibility should circumstances arise that cause a shift in the academic calendar. In this event, Community Advisors will be notified as to any impact on the employment dates and time frame as soon as possible and once those shifts are finalized. In the spirit of professional courtesy and etiquette, please notify all supervisors, coaches, or anyone who may be impacted by these dates so you do not have any conflicts for training. This includes outside/family activities, employment, and/or any other college-related positions, activities, or athletics. All travel arrangements must be made with an understanding of the training date requirements.

        Should you have any questions or concerns regarding this offer that might affect your acceptance, please contact Kyle Arthenayake, Associate Director of Residential Education (karthena@colby.edu) or Shikha Shrestha, Assistant Director of Residential Education (shshrest@colby.edu). 

        Once again, congratulations! I look forward to working with you on Hall Staff next year.

        Sincerely,
        Colby's Office of the Residential Experience (CORE)
        """
    elif result == "Waitlisted":
        subject = "CA Alternate Offer"
        body = f"""
        {preferred_name} {last_name}
        {student_id}

        Dear {preferred_name},

        On behalf of the Office of Residential Experience, I would like to take this opportunity to thank you for your interest and participation in the Community Advisor selection process. This year's selection process for the Community Advisor position was extremely competitive, particularly given the quality of applicants seeking a role. This made position deliberations incredibly difficult. 

        After a complete assessment of our positions and communities and a full review of all potential candidates, we are unfortunately unable to offer you an official position at this immediate time. However, we are pleased to offer you an Alternate Community Advisor position. Our interview team was impressed with your skills, experiences, and enthusiasm, and we believe you have the skills to be a Community Advisor.

        Why should you consider the Alternate Community Advisor status?
        The role of the Alternate Community Advisor (CA) is critical if a CA position becomes available for the upcoming academic year
        It is not uncommon that Alternate Community Advisors may receive an offer as early as TBD, or throughout the summer (should positions become available).
        If a Community Advisor position does become available (including those created by CAs going abroad), we will consider our Alternate Community Advisor pool to choose a replacement.
        If a position becomes available, you will be considered if we believe you would be a good fit for the particular staff and floor/building community with the opening.

        In order to share your decision regarding this offer, please complete the following:
        Electronically accept or decline the offered position by no later than TBD

        Please understand that this is a conditional position offer. Serving as an Alternate Community Advisor for the upcoming academic year is contingent upon the successful completion of the following:
        Maintaining a minimum 2.50 cumulative grade point average (GPA) - GPAs will be checked after each semester. If you do not meet the GPA requirement, you will be notified; and
        Remaining in good student conduct standing with the College.

        Something to Keep in Mind: As an Alternate Community Advisor, you may receive an offer for a position. As such, all Community Advisors for the 2025-2026 academic year will be required to attend Fall Hall Staff Training beginning as early as TBD. Training and move-in preparations would continue through the first day of classes. Please be mindful of these dates should you receive an offer at any point.

        At any time after accepting this role, if you would like to remove yourself from consideration (due to accepting another position, no longer being interested, or for any other reason) or if you have any questions, please feel free to contact Kyle Arthenayake, Associate Director of Residential Education (karthena@colby.edu) or Shikha Shrestha, Assistant Director of Residential Education (shshrest@colby.edu). 

        Sincerely,
        Colby's Office of the Residential Experience (CORE)
        """
    else:  # Rejected
        subject = "CA Regret Letter"
        body = f"""
        {preferred_name} {last_name}

        Dear {preferred_name},

        Thank you for your participation in the Community Advisor Selection Process. We appreciate your interest, application, and investment in the process. This year's selection process for Community Advisor positions was extremely competitive, particularly given the quality of applicants. This made position deliberations incredibly difficult. 

        After a complete and thorough assessment of the Hall Staff team's needs and after a full review of all potential candidates, I regret to inform you that the Office of the Residential Experience cannot offer you a Community Advisor position at this time.
 
        Thank you again for your time, energy, and commitment to the Apartment Community Advisor selection process. Should you have any questions please don't hesitate to reach out.

        Sincerely,
        Colby's Office of the Residential Experience (CORE)
        """
    
    return send_email(applicant_email, subject, body)
