import re

def is_email_address(email):

    local = r'^(?!\.)((?!\.\.)[a-zA-Z0-9\.#!%\$‘&\+\*–\/=\?\^_`\{\|}~])+(?<!\.)$'
    domain = r'^(?![\.\-])((?!\.\.)[a-zA-Z0-9\.\-])+(?<![\.\-])$'

    loc = email.split('@')[0]
    dom = email.split('@')[1]
    
    if re.match(local, loc) and re.match(domain, dom):
        return True
    else:
        return False

if __name__ == "__main__":
    emails = ['dairdharris1@gsu.edu', 'd.aird.harris1@gsu.edu', '.dairdharris1@gsu.edu', 'dairdharris1.@gsu.edu', 'dairdharris1@g-s-u.edu', 'dairdharris1@-gsu.edu']
    for email in emails:
        print(email, is_email_address(email))
