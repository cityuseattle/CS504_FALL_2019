import smtplib
import getpass

smtp_server = 'smtp-mail.outlook.com'
port = 587
sender = 'examplesmtp@outlook.com'
recipient = 'examplesmtp@outlook.com'
passwd = getpass.getpass('Password:')
msg = """Subject: No problem
Hi
"""
try:
    smtp_obj = smtplib.SMTP(smtp_server, port)
    smtp_obj.ehlo()
    print(smtp_obj.starttls())
    print(smtp_obj.login(sender, passwd))
    smtp_obj.sendmail(sender, recipient, msg)
except Exception as e:
    print("Cannot send email:",e)
finally:
    print(smtp_obj.quit())