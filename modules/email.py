import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_email: str, subject: str, body: str):
    # Configure with your SMTP
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = "noreply@supashop.co.ke"
    smtp_password = "your_app_password"

    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, to_email, msg.as_string())
        server.quit()
        return {"status": "sent"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}
