email = input("Enter your Email address: ").strip()

username = email[:email.index('@')]
domain = email[email.index('@') + 1 :]

count = 0
for char in username:
    if char.isalpha():
        count += 1

print(f"Your username is {username} & domain is {domain}")
print(f"Your username have {count} characters.")