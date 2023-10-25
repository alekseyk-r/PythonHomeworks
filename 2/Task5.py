def extract_login():
    email = input()
    return email.split('@')[0]

print(extract_login())
