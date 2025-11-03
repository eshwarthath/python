def minion_game(string):
    stuart = 0
    kevin = 0
    n = len(string)

    vowels = "AEIOU"
    for i in range(n):
        points = n - i
        if string[i] in vowels:
            kevin += points
        else:
            stuart += points

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")
 

if __name__ == '__main__':
    s = input()
    minion_game(s)
