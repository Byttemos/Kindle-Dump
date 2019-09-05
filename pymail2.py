#!/usr/bin/env python
import smtplib
from email.message import EmailMessage
import os
import time

EMAIL_ADDRESS = "INSERT EMAIL"
EMAIL_PASS = "INSERT PASSWORD"

doc_count = os.system("cd ~/tokindle && lsd")

while 1 == 1:

    if len(os.listdir("/home/henrik/tokindle")) == 0:
        time.sleep(5)
        continue
    
    else:

        for doc in os.listdir("/home/henrik/tokindle"):
            msg = EmailMessage()
            msg["Subject"] = "To kindle"
            msg["From"] = EMAIL_ADDRESS
            msg["To"] = "INSERT KINDLE EMAIL"
            msg.set_content("")


            with open("/home/henrik/tokindle/" + doc , "rb") as f:
                file_data = f.read()
                file_name = f.name
                short_name = file_name.lstrip("/home/henrik/tokindle/")


                msg.add_attachment(file_data, maintype = "pdf", subtype = "pdf", filename = short_name)

                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
#with smtplib.SMTP("localhost", 1025) as smtp:

                    smtp.login(EMAIL_ADDRESS, EMAIL_PASS)

                    smtp.send_message(msg)
        

            os.remove("/home/henrik/tokindle/" + doc)
