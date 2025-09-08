# Create 3 dictionaries for 3  Students
student1 = {'Name': 'Shuvajit', 'Age': 23,'Sub':'Java'}
student2 = {'Name': 'Ayush', 'Age': 21,'Sub':'Python'}
student3 = {'Name': 'Susamanja', 'Age': 22,'Sub':'C++'}

# Store them in a list
students = [student1, student2, student3]

# Print name and age of each student
for student in students:
    print("Name:", student['Name'])
    print("Age:", student['Age'])
    print("Subject:", student['Sub'])
    print()