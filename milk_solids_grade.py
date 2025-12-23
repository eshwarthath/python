A,B=map(int,input().split())
milk_solids=A+B
if milk_solids>=15 and B>=8:
    print(1)
elif milk_solids>=10 and B>=3:
    print(2)
elif milk_solids>=3:
    print(3)
else:
    print(4)
