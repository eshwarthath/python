
from itertools import product

list_1 = list(map(int, input().split()))
list_2 = list(map(int, input().split()))

result = product(list_1, list_2)


print(*result)
