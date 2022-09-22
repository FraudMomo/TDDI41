from random import randint, choice
from unicodedata import normalize
import subprocess
import string
import sys

userlist = sys.stdin

# List of intial system users
file = open("/etc/passwd", "r")
system_users = [line.split(':')[0] for line in file.readlines()]

generated_usernames = []


def generate_username(name):
    # Get first letters of first and last name
    name = name.lower().split()
    firstname = name[0]
    lastname = name[1] if len(name) > 1 else ''
    initials = firstname[0:3] + lastname[0:3]

    # Generate random number
    number = randint(100, 999)

    username = ''
    # Check for invalid characters
    for c in initials:
        username += 'a' if c not in string.ascii_letters else c

    # Final username is username + number
    final_username = username + str(number)

    # Check if username exists => generate new number
    while final_username in (generated_usernames or system_users):
        number = randint(100, 999)
        final_username = username + str(number)

    # Add username to list
    generated_usernames.append(final_username)

    return final_username


def generate_password():
    # Password length between 10 and 20
    length = randint(10, 20)
    password = ''

    # Generate a random password from ascii
    for _ in range(length):
        password += choice(string.ascii_letters)
    return password


chpasswd_list = []

for name in userlist:
    if name.strip() == '':
        continue

    # Generate username and password
    username = generate_username(name)
    password = generate_password()

    # Create user with a home directory
    subprocess.run(['useradd', '-m', username])

    # Save username and password to chpasswd list
    chpasswd_list.append(username + ':' + password)

    print(username, password)

# Set password of users
changePassword = subprocess.Popen(['chpasswd'], stdin=subprocess.PIPE)
changePassword.communicate('\n'.join(chpasswd_list).encode('utf-8'))
