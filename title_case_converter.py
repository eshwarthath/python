s = input("enter a string: ")

words = s.split()

final = []

for word in words:
    capitalized = word[0].upper() + word[1:].lower()
    final.append(capitalized)

print(" ".join(final))
