import matplotlib.pyplot as plt
import json as js

with open('labels.json', 'r+') as file:
    data = js.load(file)

marks = []
subjects = []
i = len(data)-1
for j in data[i]['data']:
    marks.append(float(j['percent']))
    subjects.append(j['subject'])

ytick = [10,20,30,40,50,60,70,80,90,100]
plt.title('Marks Analysis Bar Graph',fontdict={'fontname':'Comic Sans MS'})
plt.yticks(ytick)
plt.bar(subjects, marks, color='red', width=0.05)
plt.plot(marks, marker = 'o')
plt.show()
