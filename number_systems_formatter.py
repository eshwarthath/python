def print_formatted(number):
    width = len(bin(number)[2:])   # length of binary representation of the max number
    for i in range(1, number + 1):
        deci = str(i).rjust(width)
        octa = oct(i)[2:].rjust(width)
        hexa = hex(i)[2:].upper()[2:].rjust(width)
        bina = bin(i)[2:].rjust(width)
        print(deci, octa, hexa,   bina)


n = int(input())
print_formatted(n)
