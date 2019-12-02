import imaplib
import getpass
import email


imap_host = 'imap-mail.outlook.com'
user = 'examplesmtp@outlook.com'
port = 993

passwd = getpass.getpass('Password: ')

try:
    mail = imaplib.IMAP4_SSL(imap_host)
    mail.login(user, passwd)
    mail.select('inbox')

    status, data = mail.search(None, 'ALL')
    inbox_item = data[0].split()
    most_recent = inbox_item[-1]

    status2, email_data = mail.fetch(most_recent, '(RFC822)')
    print(status2)

    raw_email = email_data[0][1]
    msg = email.message_from-bytes(raw_email)
    print("From: ", msg['From'])
    print("Subject: ", msg['Subject'])
    print(msg.get_payload())
except Exception as e:
    print("Cannot access email")
    print(e)
finally:
    mail.logout()
    