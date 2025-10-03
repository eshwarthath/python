def integer():
    while True:
        try:
            sentence = int(input("Enter a sen:  "))
            print("you have written correct integer")
            return sentence

        except ValueError:
            print("print a valid integer")
correct = integer()
print(correct)

