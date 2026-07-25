email = input("Enter your email address: ").strip()

username, domain = email.split('@')[0], email.split('@')[-1]

if '.' in domain:
    domain_name, extension = domain.split('.', 1)
    print(f"Username: {username}")
    print(f"Domain Name: {domain_name}")
    print(f"Extension: {extension}")
else:
    print("Invalid email format. Please ensure the domain contains a '.' character.")