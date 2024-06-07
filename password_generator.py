import secrets
import string


def generatePass(length):
    # Defining the characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure password complexity
    password = []
    password.append(secrets.choice(string.ascii_lowercase))
    password.append(secrets.choice(string.ascii_uppercase))
    password.append(secrets.choice(string.digits))
    password.append(secrets.choice(string.punctuation))

    for _ in range(length):
        password.append(secrets.choice(characters))

    # Shuffling the list
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


def checkLength(length):
    # Check if the length is between 6 and 20
    if length < 6 or length >= 20:
        print("Password length must be between 6 and 16 characters")
    else:
        generated_pass = generatePass(length)
        print("Generated password: ", generated_pass)


if __name__ == '__main__':
    # Enter length of the password
    pass_length = int(input("Enter length of the password: "))

    # Function to check the length of the password
    checkLength(pass_length)
