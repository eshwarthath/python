def solve(s):
    result = []
    capitalize_next = True

    for ch in s:
        if ch == " ":
            result.append(ch)
            capitalize_next = True
        elif capitalize_next:
            result.append(ch.upper())
            capitalize_next = False
        else:
            result.append(ch)

    return "".join(result)
