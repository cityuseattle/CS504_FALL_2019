import smtplib
import getpass

smtp_server = 'smtp.gmail.com'
port = 587 # port 587 uses TLS encryption
sender = 'jaipreet.toor@gmail.com'
recipient = 'jaipreet.toor@gmail.com'
# This allows you to type password without showing it
passwd = getpass.getpass('Password: ')
msg = '''Subject: Need your help!

Hi Jaipreet,
How is it going?
I am so sleepy right now, but I need your help with this.

When I tell you to pick up the left rock,
it will be the right one, and then only the right rock will be left.
So, left or right?

I'm going to bed, sweet dreams!
'''
try:
    smtp_obj = smtplib.SMTP(smtp_server, port)
    # indentify yourself to the SMTP server
    smtp_obj.ehlo()
    # if you use port 465 (SSL), encryption is already set up. No need to call starttls()
    print(smtp_obj.starttls())
    print(smtp_obj.login(sender, passwd))
    smtp_obj.sendmail(sender, recipient, msg)
except Exception as e:
    print('Cannot send email:', e)
finally:
    print(smtp_obj.quit())