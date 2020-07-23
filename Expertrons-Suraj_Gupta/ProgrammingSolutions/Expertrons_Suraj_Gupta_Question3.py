#solution of problem 3
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.22], ['Akriti', 41], ['Harsh', 39]] 
students.sort()

unique_grades = set([each_grades[1] for each_grades in students])

unique_grades.discard(max(unique_grades))

second_lowest_grade = min(unique_grades)

for each_grade in students:
    if each_grade[1] == second_lowest_grade:
        print(each_grade[0])
