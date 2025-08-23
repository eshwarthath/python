n = input("enter a number: ")

even_sum = 0
odd_sum = 0

for ch in n:

    digit = int(ch)

    if digit % 2 == 0:
        even_sum += digit

    else:
        odd_sum += digit

print(even_sum, odd_sum)




