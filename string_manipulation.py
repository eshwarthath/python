sentence = input("Enter a sentence to swap:  ").lower()
if len(sentence) < 2:
    print(sentence)
else:
    list_sentence = list(sentence)
    list_sentence[0], list_sentence[-1] = list_sentence[-1], list_sentence[0]
    final_sentence = "".join(list_sentence)
    print(final_sentence)
