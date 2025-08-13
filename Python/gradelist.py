students = []
grades = []

def add_student(name, grade):
    students.append(name)
    grades.append(grade)

def update_grade(name, grade):
    if name in students:
        idx = students.index(name)
        grades[idx] = grade

def remove_student(name):
    if name in students:
        idx = students.index(name)
        students.pop(idx)
        grades.pop(idx)

def average_grade():
    return sum(grades) / len(grades) if grades else 0

def highest_grade():
    return max(grades) if grades else None

def lowest_grade():
    return min(grades) if grades else None

# Example usage:
add_student("Sandhyarani", 85)
add_student("Diksha", 90)
update_grade("Sandhyarani", 88)
remove_student("Diksha")

print("Average grade:", average_grade())
print("Highest grade:", highest_grade())
print("Lowest grade:", lowest_grade())
