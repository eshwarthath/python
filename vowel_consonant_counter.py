sentence = input("Enter a sentence: ").lower()  

vowels = 0
consonants = 0

for char in sentence:
    if char.isalpha():
        if char in "aeiou":
            vowels += 1
        else:
            consonants += 1

print(f"Vowels: {vowels}, Consonants: {consonants}")
