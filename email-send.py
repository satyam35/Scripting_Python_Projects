import smtplib
from email.message import EmailMessage
email=EmailMessage()
email['from']="Satyam Singh"
email['to']='202020satyamsingh@gmail.com'
email['subject']='You won 10000 Rupees'
email.set_content('I m python master')
with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('202020satyamsingh@gmail.com','9628653416')
    smtp.send_message(email)
    print("All done")

