string = input("Enter a string: ").lower()
substring = input("Enter a substring: ").lower()
def result(string,substring):
    results = string.count(substring)
    print(f"there are {results} substrings in this string")
    return
result(string,substring)
