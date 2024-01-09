# str.startswith() and .endswith()

# @gmail.com @yahoo.com @outlook.com @msn.com
email_postfixes = tuple(input("Email Postfixes: ").split(" "))

email = input("Email: ")

if email.endswith(email_postfixes):
    print("Valid Email!")
else:
    print("Invalid Email!")
