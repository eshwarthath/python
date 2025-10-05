student_score = {}
highest_score = 0
highest_student = []
student = 0
score = 0
choice = int(input("enter how many students do you want to check their score: "))

while choice:
    student = input("Enter your name: ")
    score = float(input("Enter your score: "))
    student_score[student] = score

    if score >= highest_score:
        highest_score = score
        highest_student.append(student)

    choice -= 1

print(f"\nstudents dictionary = {student_score}")
print(f"Your highest score is {highest_score} and the students are {highest_student}")












