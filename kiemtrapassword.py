def checkStrongPassword(password):
    if len(password) < 6:
        return False
    num = False
    low = False
    up = False
    special = False
    for i in password:
        if i.isalnum():
            num = True
    if i.islower():
        low = True
    if i.isupper():
        up = True
    if i in '!@#$%^&*()-+':
        special = True
    return num and low and up and special