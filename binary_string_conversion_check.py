# Program to check if one binary string can be converted to another by swapping characters
t = int(input())

for _ in range(t):
    n=int(input())
    s1=str(input())
    s2=str(input())
    
    # Count number of 1's and 0's in both strings
    if s1.count('1') == s2.count('1') and s1.count('0') == s2.count('0'):
        print("YES")
    else:
        print("NO")
