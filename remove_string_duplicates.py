def merge_the_tools(string):
    result = ""
    for ch in string:
        if ch not in result:
            result += ch
    print(result)

string = input("enter a string: ")
merge_the_tools(string)
