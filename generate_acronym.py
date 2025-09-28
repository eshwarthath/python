phrase = input("Enter a phrase: ")
acronyms = ""
words = phrase.split()
for word in words:
    acronyms = acronyms + word[0].upper()
print(acronyms)
