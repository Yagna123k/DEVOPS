# score = int(input("Enter your score: "))

# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")


# student_grades = {}

# while True:
#     print("\nChoose an option:")
#     print("1. Add student")
#     print("2. Update grade")
#     print("3. Print all grades")
#     print("4. Exit")

#     choice = input("Enter your choice (1-4): ")

#     if choice == "1":
#         name = input("Enter student name: ")
#         grade = input("Enter grade: ")
#         if name in student_grades:
#             print(f"{name} already exists.")
#         else:
#             student_grades[name] = grade
#             print(f"Added {name} with grade {grade}.")
    
#     elif choice == "2":
#         name = input("Enter student name: ")
#         if name in student_grades:
#             grade = input("Enter new grade: ")
#             student_grades[name] = grade
#             print(f"Updated {name}'s grade to {grade}.")
#         else:
#             print(f"{name} does not exist.")
    
#     elif choice == "3":
#         if not student_grades:
#             print("No student records found.")
#         else:
#             print("Student Grades:")
#             for name, grade in student_grades.items():
#                 print(f"{name}: {grade}")
    
#     elif choice == "4":
#         print("Goodbye!")
#         break
    
#     else:
#         print("Invalid choice. Please try again.")


# file = open("example.txt", "w")

# file.write("Hello!\n")
# file.write("This is a sample text file.\n")
# file.write("You can write anything you want here.\n")

# file.close()

# print("Content written to example.txt successfully.")

file = open("example.txt", "r")

content = file.read()

print("File Content:\n")
print(content)

file.close()
