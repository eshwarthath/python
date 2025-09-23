
from itertools import product

list_1 = []
list_2 = []

a,b = map(int,input().split())
list_1.append(a)
list_1.append(b)

c,d = map(int,input().split())
list_2.append(c)
list_2.append(d)

print(list(product(list_1,list_2)))
