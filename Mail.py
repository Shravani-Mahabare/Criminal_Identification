# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 10:56:43 2024

@author: admin
"""

import smtplib
from email.message import EmailMessage

import smtplib
from email.message import EmailMessage

SENDER_EMAIL = "divyaingale011@gmail.com"
APP_PASSWORD = "drke dczf zkan iutu"


print("Mail Start")
msg = EmailMessage()
msg['Subject'] = "Message Alert"
msg['From'] = SENDER_EMAIL
msg['To'] = "divyaingale011@gmail.com"
msg.set_content('Criminal detected')

# with open('/home/pi/Face_Attendance_with_Excel_Sheet/Student_to_excel.xls', 'rb') as f:
#         file_data = f.read()
# msg.add_attachment(file_data, maintype="application", subtype="vnd.ms-excel", filename='/home/pi/Face_Attendance_with_Excel_Sheet/Student_to_excel.xls')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)
        print("Mail send successfully")

