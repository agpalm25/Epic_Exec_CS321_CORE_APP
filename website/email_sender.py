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
