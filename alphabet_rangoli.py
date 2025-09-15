def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
    # Create each row
    lines = []
    for i in range(size):
        left = alpha[size - 1:i:-1]  # descending part
        center = alpha[i:size]  # ascending part
        row = "-".join(left + center)  # join with '-'
        lines.append(row.center(4 * size - 3, "-"))  # padding with '-'

    # Print top + middle + bottom
    print('\n'.join(lines[::-1] + lines[1:]))


# Example:
n = int(input("Enter size: "))
print_rangoli(n)
