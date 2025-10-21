
def swap_case(s):
    swap_name = ""
    for i in s:
        if i == i.lower() :
            swap_name = swap_name + i.upper()
        else:
            swap_name = swap_name + i.lower()
    
    return swap_name

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
