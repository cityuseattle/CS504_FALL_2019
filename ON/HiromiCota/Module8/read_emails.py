import imaplib
import getpass
import email


# connection info
imap_host = 'imap-mail.outlook.com'
user = 'nope@nope.nope'
# Again, the class' GitHub is publicly readable. There's no reason to expose our email addresses
port = 993
passwd = getpass.getpass('Password: ')
try:
    mail = imaplib.IMAP4_SSL(imap_host)
    mail.login(user, passwd)
    mail.select('inbox')
    status, data = mail.search(None, 'ALL')
    status2, email_data = mail.fetch(most_recent, '(RFC822)')
    print(status2)
    raw_email = email_data[0][1]
    msg = email.message_from_bytes(raw_email)
    print("From:", msg['From'])
    print("Subject:", msg['Subject'])
    print(msg.get_payload())
except Exception as e:
    print("Cannot access email.")
    print(e)
finally:
    mail.logout()