if __name__ == '__main__':
    s = input()

    # 1. Alphanumeric
    if any(c.isalnum() for c in s):
        print("True")
    else:
        print("False")

    # 2. Alphabetical
    if any(c.isalpha() for c in s):
        print("True")
    else:
        print("False")

    # 3. Digits
    if any(c.isdigit() for c in s):
        print("True")
    else:
        print("False")

    # 4. Lowercase
    if any(c.islower() for c in s):
        print("True")
    else:
        print("False")

    # 5. Uppercase
    if any(c.isupper() for c in s):
        print("True")
    else:
        print("False")
