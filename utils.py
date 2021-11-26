from app import app, logging
import random, math, string, re

from utils import *

from email_validator import validate_email, EmailNotValidError

from dateutil.relativedelta import relativedelta
import datetime

#Email_validation
def email_validation(email):
    email = email.strip()
    try:
        validate_email(email)
        return True
    except EmailNotValidError as e:
        return False

#mobile_no validation
def mobile_no_validation(number):
    number = str(number)
    number = number.strip()
    if number.isnumeric() and len(number) <= 16 and len(number) > 6 :
        return True
    else:
        return False 

#char_validation
def char_validation(string):
    string = string.strip()
    regex = re.compile("[@_!#.,$%^&*()<>?/\|}{~:0-9]")
    if regex.search(string)==None and len(string) <= 64 :
        return True
    else:
        return False    

# Strong Password Valiadation
def strong_password_validation(password): 
    message = ""
    try:
        if len(password) < 8:
            message = "Password should be at least 8 characters : 8-16"
        elif len(password) > 16:
            message = "Password should not exceed 15 characters : 8-16"
        elif not re.search("[a-z]", password):
            message = "Password should contain at least one lowercase : a-z"
        elif not re.search("[A-Z]", password):
            message = "Password should contain at least one uppercase : A-Z"
        elif not re.search("[0-9]", password):
            message = "Password should contain at least one digit : 0-9"
        elif not re.search("[$#@!%^&*()]", password):
            message = "Password should contain at least one character : $#@!%^&*()"
    except Exception as e:
        logging.error("strong_password_validation : exception : {}".format(e))
        message = ""
    return message    