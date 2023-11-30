import argparse
import smtplib
from datetime import date
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email_from_outlook(sender, email_password, report, receivers):
    password = email_password
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = ", ".join(receivers)
    message["Subject"] = "Automation daily report" + ": " + str(date.today())

    html_content = """<html>
             <head></head>
             <body>
                 <p>Please find the daily report in attachment to this email.</p>
             </body>
             </html>"""

    html_body = MIMEText(html_content, "html")
    message.attach(html_body)

    # Attach file
    attachment_path = report
    attachment = open(attachment_path, "rb")
    file_attachment = MIMEApplication(attachment.read())
    file_attachment.add_header("Content-Disposition", f"attachment; filename={attachment.name}")
    message.attach(file_attachment)
    attachment.close()

    # Connect to SMTP server and send the email
    with smtplib.SMTP("smtp-mail.outlook.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receivers, message.as_string())

    print("Email sent!")


if __name__ == "__main__":
    """
    Script run example:
    python3 utils/email_sender.py $address $password allure.html email1@com, email2@com
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("email")
    parser.add_argument("password")
    parser.add_argument("attachment")
    parser.add_argument("recipients", nargs="+")
    args = parser.parse_args()

    print(args.recipients)
    send_email_from_outlook(args.email, args.password, args.attachment, args.recipients)
