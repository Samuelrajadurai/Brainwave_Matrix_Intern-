import re
weak_passwords = ["password", "12345678", "qwerty123", "password123", "admin123", "welcome123"]
password = input("Enter your password: ")
if len(password) < 8:
    print("Password must be at least 8 characters long.")
elif not re.search("[A-Z]", password):
    print("Password must contain at least one uppercase letter.")
elif not re.search("[a-z]", password):
    print("Password must contain at least one lowercase letter.")
elif not re.search("[0-9]", password):
    print("Password must contain at least one number.")
elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    print("Password should include at least one special character for better security.")
else:
    lower_pass = password.lower()
    if lower_pass in weak_passwords:
        print("Password meets the criteria but is too simple or commonly used. Try making it more complex.")
    elif re.fullmatch(r'(.)\1*', password):
        print("Password meets the criteria but uses repeated characters. Try adding more variety.")
    else:
        print("Password is strong.")
