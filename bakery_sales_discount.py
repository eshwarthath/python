# Program to calculate bakery sales details
loaves = int(input())
bread_price = 185
regular_price = loaves * bread_price
amount_discounted = regular_price * 0.60
amount_to_be_paid = regular_price - amount_discounted

print(f"Regular Price={regular_price}")
print(f"Amount Discounted={amount_discounted:.2f}")
print(f"Amount to be paid={amount_to_be_paid:.2f}")
