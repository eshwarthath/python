if __name__ == '__main__':
    n = int(input())
    command_list = []

    def command_append(num):
        command_list.append(num)

    def command_print():
        print(command_list)

    def command_sort():
        command_list.sort()

    def command_pop():
        if command_list:   # avoid popping from empty list
            command_list.pop()

    def command_reverse():
        command_list.reverse()

    def command_remove(num):
        if num in command_list:
            command_list.remove(num)

    def command_insert(i, e):
        command_list.insert(i, e)

    while n:
        a = input().split()
        command = a[0]

        if command == 'append':
            command_append(int(a[1]))

        elif command == 'print':
            command_print()

        elif command == 'sort':
            command_sort()

        elif command == 'pop':
            command_pop()

        elif command == 'reverse':
            command_reverse()

        elif command == 'remove':
            command_remove(int(a[1]))

        elif command == 'insert':
            command_insert(int(a[1]), int(a[2]))

        n -= 1
