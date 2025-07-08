import smtplib
from email.message import EmailMessage

def send_email_alert(subject, body):
    EMAIL_ADDRESS = "zbazil302@gmail.com"
    EMAIL_PASSWORD = "BAZILBROyouareseenbro@321"

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = "hrkgamer444@gmail.com"
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print("[+] Email alert sent.")
    except Exception as e:
        print(f"[!] Email failed: {e}")
