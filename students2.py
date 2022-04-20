import random

students = [
    {
        "name": "Sally Jones",
        "grade": 2
    },
    {
        "name": "Chris Smith",
        "grade": 3
    },
    {
        "name": "Sarah Thompson",
        "grade": 6
    }
]

for index in range(len(students)):
    random_number_1 = random.randint(0,9)
    random_number_2 = random.randint(0,9)
    random_number_3 = random.randint(0,9)
    student_id = f"{students[index]['name'][:3].upper()}-{random_number_1}{random_number_2}{random_number_3}"
    students[index]["student_id"] = student_id
    print(students[index])
    #print(student_id)

print(students)
