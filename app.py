from os import getenv
from collections import Counter
from imbox import Imbox
from rich.console import Console
from rich.table import Table


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

table = Table(title="Unread Email Counter")

table.add_column("Emai", style="cyan", justify="left", no_wrap=True)
table.add_column("Count", style="magenta", justify="center",)

for c in count.most_common(1000):
    table.add_row(c[0], str(c[1]))


console = Console()
console.print(table)
