
sentence = input("Enter a sentence: ")
normal_sentence = sentence.replace(" ","").lower()
reversed_sentence = normal_sentence[::-1]

if normal_sentence == reversed_sentence:
    print("palindrome")
else:
    print("not a palindrome")





