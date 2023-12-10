import re


def if_email_valid(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if re.fullmatch(regex, email):
        return True

    return False


def if_data_valid(data):
    if data.get('password') != data.get('password-confirm'):
        return False, {"message": "Passwords don't match."}
    elif not if_email_valid(data.get('email')):
        return False, {"message": "Email format isn't valid."}

    return (True,)
