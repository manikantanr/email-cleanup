from os import getenv
from collections import Counter
from imbox import Imbox
from tabulate import tabulate


IMAP_SERVER = getenv('IMAP_SERVER', 'imap.gmail.com')
EMAIL = getenv('EMAIL', '')
PASSWORD = getenv('PASSWORD', '')

emails = []

with Imbox(IMAP_SERVER,
        username=EMAIL,
        password=PASSWORD,
        ssl=True,
        ssl_context=None,
        starttls=False) as imbox:

    unread_inbox_messages = imbox.messages(unread=True)

    for uid, message in unread_inbox_messages:
    # Every message is an object with the following keys
        emails.append(
            message.sent_from[0]['email']
        )

count = Counter(emails)

print(tabulate(count.items(), headers = ['Email', 'Count']))  
