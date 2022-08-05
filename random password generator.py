import random


def random_password(length):
    chars = [str(x) for x in range(10)]  # numbers

    # adding lowercase latters
    start = "a"
    for i in range(26):
        chars.append(start)
        start = chr(ord(start) + 1)

    # adding UPPERcase latters
    start = "A"
    for i in range(26):
        chars.append(start)
        start = chr(ord(start) + 1)

    # adding special characters
    chars += ["!", "@", "#", "$", "%", "&", "*"]

    password = ""
    for i in range(length):
        password += random.choice(chars)

    return password


n = int(input("Password length: "))
print("\n")
for i in range(10):
    print(random_password(n))
print("\n")
