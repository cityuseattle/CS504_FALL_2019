import smtplib
import getpass


stmp_server = 'smtp-mail.outlook.com'
port = 587
# Our class GitHub is publicly readable. Putting private email addresses in plaintext is a bad idea
sender = 'examplesmtp@outlook.com'
recipient = 'examplesmtp@outlook.com'
passwd = getpass.getpass('Password: ')
msg = """Subject: Need your help

Hi,

This email won't go anywhere and that's OK.
Putting private email addresses in plaintext is not a great idea. 
This isn't a security class, but CS grad students and professors should know better.

Regards
"""
try:
    smtp_obj = smtplib.SMTP(stmp_server, port)
    smtp_obj.ehlo()
    print(smtp_obj.starttls())
    print(smtp_obj.login(sender, passwd))
    smtp_obj.sendmail(sender, recipient, msg)
except Exception as e:
    print("Cannot send email:", e)
finally:
    print(smtp_obj.quit())