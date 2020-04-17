# Unread Email analyser

Tool to list the stats of your unread emails, comes handy in email cleanup tasks

# Requirements

Python (3.3, 3.4, 3.5, 3.6)




# Dependencies Installation

`pip install imbox`


# Usage

```bash
expot IMAP_SERVER=imap.gmail.com
expot EMAIL=''
expot PASSWORD=''

or

set IMAP_SERVER=imap.gmail.com
set EMAIL=''
set PASSWORD=''



python app.py


```


# Password notes

Using this with Gmail might cause few problems due `Insecure Apps` and Two-Factor Authentication fetures. Create app specific password from Google account to use this tool.

https://myaccount.google.com/apppasswords
