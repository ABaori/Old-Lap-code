import os

import Functions as func

USER_CHOICE = """
ENTERED VALUE : MEANING
a : add a label
q: exit

ENTER YOUR CHOICE""
"""

subjects = ['Maths', 'Physics', 'English', 'Chemistry', 'Computer']


def menu():
    if not os.path.exists('labels.json'):
        func.create_file()

    command = input(USER_CHOICE)
    temp = []
    while command != 'q':
        if command == 'a':
            name = input("Enter your name:")
            Paper = input("Enter Paper type Out of CT1,CT2,CT3,SEM1,SEM2:")
            func.add_labels(name,Paper)
            for subject in subjects:
                marks = int(input(f"Enter marks in {subject}"))
                total_marks = int(input(f"Enter total marks of {subject}"))
                func.add_data(subject, marks, total_marks)

        command = input(USER_CHOICE)


menu()
func.suggestions()