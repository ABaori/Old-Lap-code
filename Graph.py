import matplotlib.pyplot as plt
import func_graphs as _
import json as js

import os

User_choice = """
1.Ct1
2.Ct2
3.Ct3
4.Sem1
5.Sem2
Choose any option from 1-5:
"""


subjects = ['Maths','Physics','English','Chemistry','Computer']

subject_marks = []

def User_Interface():
    global total_percent
    total_percent = 0
    User_inpt = int(input(User_choice))

    if User_inpt==1:

        for i in subjects:
            total_marks = int(input(f"Total marks for subject {i}"))
            marks = int(input(f"Enter your marks in subject {i}"))

            percent = marks/total_marks*100
            subject_marks.append(percent)
            total_percent += percent/5

    if User_inpt==2:
        for i in subjects:
            total_marks = int(input(f"Total marks for subject {i}"))
            marks = int(input(f"Enter your marks in subject {i}"))

            percent = marks / total_marks * 100
            subject_marks.append(percent)
            total_percent += percent / 5

    if User_inpt==3:
        for i in subjects:
            total_marks = int(input(f"Total marks for subject {i}"))
            marks = int(input(f"Enter your marks in subject {i}"))

            percent = marks / total_marks * 100
            subject_marks.append(percent)
            total_percent += percent / 5

    if User_inpt==4:
        for i in subjects:
            total_marks = int(input(f"Total marks for subject {i}"))
            marks = int(input(f"Enter your marks in subject {i}"))

            percent = marks / total_marks * 100
            subject_marks.append(percent)
            total_percent += percent / 5

    if User_inpt==5:
        for i in subjects:
            total_marks = int(input(f"Total marks for subject {i}"))
            marks = int(input(f"Enter your marks in subject {i}"))

            percent = marks / total_marks * 100
            subject_marks.append(percent)
            total_percent += percent / 5

User_Interface()

# ytick = [10,20,30,40,50,60,70,80,90,100]
# plt.title('Marks Analysis Bar Graph',fontdict={'fontname':'Comic Sans MS'})
# plt.yticks(ytick)
# plt.bar(subjects, subject_marks, color='red', width=0.05)
# plt.plot(subject_marks, marker = 'o')
# plt.legend()
# plt.show()
print(total_percent)
_.give_suggestion(total_percent)