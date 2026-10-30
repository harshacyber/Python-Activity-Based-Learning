password = input("Enter password: ")

if len(password) >= 8:
    if any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password):
        print("Password is valid")
    else:
        print("Password must contain uppercase, lowercase and numbers")
else:
    print("Password must have at least 8 characters")