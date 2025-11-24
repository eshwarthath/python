# Program to count occurrences of a character in a string without using count()
s=str(input())
a=str(input())

c = 0
for i in s:
    if i == a:
        c += 1
print(c)
