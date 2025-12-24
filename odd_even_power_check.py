n=int(input())
if n%2==1:print("Odd")
elif n&(n-1)==0:print("Same")
else:print("Even")
