student = []
student_none = []

for i in range(28):
    student.append(int(input()))

for j in range(1, 31):
    if not j in student:
        student_none.append(j)

for k in range(len(student_none)):
    print(student_none[k])