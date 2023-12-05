import smtplib
import sys
import xml.etree.ElementTree as ET
from datetime import date
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path


def send_email_from_outlook(
    sender, email_password, report, service_name, junitxml_report: str, receivers
):
    def email_template(total: int, passed: int, failed: int, skipped: int) -> str:
        return (
            f"<p style='max-width: 120px'><font color='gray'> Total tests: {total}\n </p>"
            f"<p style='max-width: 120px'><font color='green'> Passed: {passed}\n </p>"
            f"<p style='max-width: 120px'><font color='red'> Failed: {failed}\n </p>"
            f"<p style='max-width: 120px'><font color='orange'> Skipped: {skipped}\n </p>"
        )

    def parse_report(xml_report: str) -> tuple:
        tree = ET.parse(xml_report)
        root = tree.getroot()[0]
        total = int(root.get("tests"))
        failed = int(root.get("failures"))
        skipped = int(root.get("skipped"))
        passed = total - failed - skipped

        return email_template(total, passed, failed, skipped)

    statistics = parse_report(junitxml_report)

    mailbox_password = email_password
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = ", ".join(receivers)
    message["Subject"] = (
        "<AQA Service> Automation daily report: " + service_name + " " + str(date.today())
    )

    html_content = f"""<html>
             <head></head>
             <body>
                 <h3>Please find the detailed report in attachment to this email.</h1>
                 <h3>{statistics}</h2>
             </body>
             </html>"""

    html_body = MIMEText(html_content, "html")
    message.attach(html_body)

    # Attach file
    attachment_path = report
    with open(attachment_path, "rb") as attachment:
        file_attachment = MIMEApplication(attachment.read())
        file_attachment.add_header(
            "Content-Disposition", f"attachment; filename={attachment.name}"
        )
        message.attach(file_attachment)
        attachment.close()

    # Connect to SMTP server and send the email
    with smtplib.SMTP("smtp-mail.outlook.com", 587) as server:
        server.starttls()
        server.login(sender, mailbox_password)
        server.sendmail(sender, receivers, message.as_string())

    print("Email sent!")


if __name__ == "__main__":
    path = Path(__file__).parent.parent
    sys.path.append(str(path))
    email = sys.argv[1]
    password = sys.argv[2]
    report_attachment = sys.argv[3]
    project_name = sys.argv[4]
    report_template = sys.argv[5]
    recipients = sys.argv[6:]

    print(recipients)
    send_email_from_outlook(
        email, password, report_attachment, project_name, report_template, recipients
    )
