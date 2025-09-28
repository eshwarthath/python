user_input = input("Please enter a word : ")
string = ""
for letter in user_input:
    if letter not in string:
        string += letter

print(string)
