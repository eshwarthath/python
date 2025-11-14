n = int(input())
x = 2 ** n
s = str(x)
sum_digits = 0
for i in s:
    sum_digits += int(i)
print(sum_digits)
