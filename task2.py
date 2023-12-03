import random
import string

def password_generator(length):
    ch = string.ascii_letters + string.digits + string.punctuation
    pw = ''.join(random.choice(ch) for _ in range(length))
    return pw

while True:
    try:
        password_len = int(input("Enter the wanted length of the password: "))
        if password_len > 0:
            break
        else:
            print("Password length should be greater than 0. Retry.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

pw = password_generator(password_len)
print(f"Generated Password: {pw}")
