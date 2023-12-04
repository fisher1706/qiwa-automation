import argparse
import smtplib
from datetime import date
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email_from_outlook(sender, email_password, report, receivers, service_name, junitxml_report: str):

    def email_template(total: int, passed: int, failed: int, skipped: int) -> str:
        return (f"<p style='max-width: 90px';><font color='grey'> Total: {total}\n </p>"
                f"<p style='max-width: 90px'><font color='green'> Passed: {passed}\n </p>"
                f"<p style='max-width: 90px'><font color='red'> Failed: {failed}\n </p>"
                f"<p style='max-width: 90px'><font color='orange'> Skipped: {skipped}\n </p>")

    def parse_report(xml_report: str) -> tuple:
        import xml.etree.ElementTree as ET

        tree = ET.parse(xml_report)
        root = tree.getroot()[0]
        total = int(root.get("tests"))
        failed = int(root.get("failures"))
        skipped = int(root.get("skipped"))
        passed = total - failed - skipped

        return email_template(total, passed, failed, skipped)

    statistics = parse_report(junitxml_report)

    password = email_password
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = ", ".join(receivers)
    message["Subject"] = "Automation daily report: " + service_name + " " + str(date.today())

    html_content = f"""<html>
             <head></head>
             <body>
                 <h3>Please find the daily report in attachment to this email.</h1>
                 <h3>{statistics}</h2>
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
    parser.add_argument("recipients", nargs = "+")
    parser.add_argument("project_name")
    parser.add_argument("report_template")
    args = parser.parse_args()

    print(args.recipients)
    send_email_from_outlook(args.email, args.password, args.attachment, args.recipients, args.project_name, args.report_template)
