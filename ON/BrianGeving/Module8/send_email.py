import smtplib
import getpass

smtp_server = 'smpt-mail.outlook.com'
port = 587
sender = 'examplesmtp@outlook.com'
recipient = 'examplesmtp@outlook.com'
passwd = getpass.getpass('Password: ')
msg = """Subject: Need your help

Hi there,
How is it going?
I am so sleepy now, but I need your help with this.

When I tell you to pick up the left rock,
it will be the right one, and then only the right rock will be left.
So, left or right?

I'm going to bed, sweet dream!
"""
try:
    smtp_obj = smtplib.SMTP(smtp_server, port)
    smtp_obj.ehlo()
    print(smtp_obj.starttls())
    print(smtp_obj.login(sender, passwd))
    smtp_obj.sendmail(sender, recipient, msg)
except Exception as e:
    print("Cannot send mail:", e)
finally:
    print(smtp_obj.quit())
    