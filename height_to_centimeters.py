# Program to convert height from feet and inches to centimeters
feet, inches = map(int, input().split())
centimeters = (feet * 12 + inches) * 2.54
print(f"Your height in centimeters is : {centimeters:.2f}")
