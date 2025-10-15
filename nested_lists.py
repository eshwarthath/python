if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())      

        students.append([name, score])

    grades = [s[1] for s in students]
    unique_grades = sorted(set(grades))
    second_lowest = unique_grades[1]

    names = [s[0] for s in students if s[1] == second_lowest]
    names.sort()

    for n in names:
        print(n)
