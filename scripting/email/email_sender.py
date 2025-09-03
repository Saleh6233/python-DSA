# Sending single email
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

# email = EmailMessage()

# email['from'] = "Saleh Ahmad Sazzad"

# email['to'] = "mehedieyh@gmail.com"

# email['subject'] = "You won 1,000,000 dollars!"
# # email['subject'] = "Email from Python;;; "

# email.set_content("I am a Python Master!")

# with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login("salehsazzad6233@gmail.com",
#              "")  # Enter Password
#     smtp.send_message(email)
#     print("Alhamdulillah")

html = Template(Path("./index.html").read_text())

email = EmailMessage()

email['from'] = "Saleh Ahmad Sazzad"

email['to'] = "anon20221111@gmail.com"

email['subject'] = "You have been asked to join CodeBandit!"


email.set_content(html.substitute({'name': "Saleh"}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("salehsazzad6233@gmail.com",
               "shvo lipv hwrw mkkd")  # Enter Password
    smtp.send_message(email)
    print("Alhamdulillah")
