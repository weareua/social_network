import os
from pyhunter import PyHunter


def check_email(email):
    hunter = PyHunter(os.getenv("HUNTER_API"))
    result = hunter.email_verifier(email)
    return result['webmail']
