sentence = input("Enter a sentence: ").lower()

result_list = []

for char in sentence:
  
    if char.isalpha():
      
        if sentence.count(char) == 1:
            result_list.append(char)
          
print(result_list)
