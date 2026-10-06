name = input("Enter your name: ")
grade = float(input("Enter your grade: "))

print("\nStudent:", name)
print("Grade:", grade)

if grade >= 90:
    print("Excellent!")
elif grade >= 80:
    print("Very Good!")
elif grade >= 75:
    print("Passed!")
else:
    print("Failed.")
