students = {
    "Aarav": 19,
    "Bhavna": 22,
    "Chirag": 20,
    "Deepika": 21,
    "Eshan": 18
}
print("Students older than 20:")
for name, age in students.items():
    if age > 20:
        print(f"{name}: {age}")
students["Farhan"] = 30
print("\nAfter adding Farhan:")
print(students)
print("\nAll students (name and age):")
for name, age in students.items():
    print(f"{name}: {age}")
del students["Eshan"]
print("\nAfter deleting Eshan:")
print(students)
total_age = sum(students.values())
average_age = total_age / len(students)
print(f"\nAverage age of students: {average_age:.2f}")
