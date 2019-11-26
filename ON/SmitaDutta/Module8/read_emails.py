import imaplib
import getpass
import email  # library for managing and parsing email messages

# connection info
imap_host = 'imap-mail.outlook.com'
user = 'examplesmtp@outlook.com'
port = 993

# this allows you to type password without showing the characters
passwd = getpass.getpass('Password: ')

# read the most recent email from INBOX
try:
    mail = imaplib.IMAP4_SSL(imap_host)
    mail.login(user, passwd)
    mail.select('inbox')
    # return status msg, return list of how many email in mailbox
    status, data = mail.search(None, 'ALL')
    inbox_item = data[0].split()
    most_recent = inbox_item[-1]
    # RFC822 is encoding, decoding format used to parse messages
    status2, email_data = mail.fetch(most_recent, '(RFC822)')
    print(status2)
    # content of the email is here
    raw_email = email_data[0][1]
    msg = email.message_from_bytes(raw_email)
    print("From:", msg['From'])
    print("Subject:", msg['Subject'])
    print(msg.get_payload())
except Exception as e:
    print("Cannot access email")
    print(e)
finally:
    # return 'BYE' response
    mail.logout()
