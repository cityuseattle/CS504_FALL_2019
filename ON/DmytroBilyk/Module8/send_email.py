import smtplib
import getpass

smtp_server = 'smtp.gmail.com'
port = 587
sender = 'examplesmtp@gmail.com'
recipient = 'examplesmtp@gmail.com'

# this allow you to type password without showing
passwd = getpass.getpass('Password: ')
msg = """ Subject: Need your help

Hi there,
How is it going?
I am so sleepy now, but I need your help with this.

When I tell you to pick up the left rock,
It will be the right one, and then only the right rock will be left.
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
    print("Cannot send email:", e)
finally:
    print(smtp_obj.quit())