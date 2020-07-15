import re


def regex_email(pattern,input_mail_id=None):
    Email_Validation = re.compile(pattern).search(input_mail_id)

    if not Email_Validation:
        print("email validation failed")
        return False

    else:
        print("Email validation is successfull") 
        return True

