# Read number of test cases
t = int(input())

# Process each string
for i in range(t):
    str1=str(input())
    lowercase = ''
    uppercase = ''
    
    # Separate lowercase and uppercase letters
    for char in str1:
        if char.islower():
            lowercase += char
        else:
            uppercase += char
    
    # Combine lowercase first, then uppercase
    sorted_string = lowercase + uppercase
    print(sorted_string)
