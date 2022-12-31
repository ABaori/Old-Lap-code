import json as js

labels_file = 'labels.json'


def create_file():
    with open(labels_file, 'w') as file:
        js.dump([], file)


def get_all_labels():
    with open(labels_file, 'r+') as file:
        return js.load(file)


def add_labels(name, paper_type):
    labels = get_all_labels()

    # name search then retrive data fied

    labels.append({'name': name, 'Paper': paper_type, 'data': []})

    _save_all_labels(labels)


def add_data(subject, marks, total_marks):
    labels = get_all_labels()
    percent = float(marks / total_marks * 100)
    labels[len(labels) - 1]['data'].append({'subject': subject,
                                            'marks': marks,
                                            'total_marks': total_marks,
                                            'percent': percent})
    _save_all_labels(labels)


def _save_all_labels(labels):
    with open(labels_file, 'w') as file:
        js.dump(labels, file, indent=4)


def suggestions():
    percent = []

    subject = []
    with open(labels_file, 'r') as file:
        data = js.load(file)
    for i in data:
        if i['Paper'] == data[len(data)-1]['Paper']:
            marks = []
            for j in i['data']:
                marks.append(j['percent'])
        percent.append(marks)
    for j in range(5):
        subject.append(i['data'][j]['subject'])

    my_marks = percent.pop()
    Maths = []
    Physics = []
    English = []
    Chemistry = []
    Computer = []
    for i in percent:
        Maths.append(i[0])
        Physics.append(i[1])
        English.append(i[2])
        Chemistry.append(i[3])
        Computer.append(i[4])
    print("SUGGESTIONS:\n")

    print("    Maths:")
    Math_rel = max(Maths)-my_marks[0]
    Eng_rel = max(English) - my_marks[2]
    Phy_rel = max(Physics) - my_marks[1]
    Chem_rel = max(Chemistry) - my_marks[3]
    Comp_rel = max(Computer) - my_marks[4]
    if Math_rel<5:
        print("      Your hard work payed off. Your very close of becoming topper of your class.Keep your way of studying the same.\n")
    if 5<= Math_rel < 10:
        print("      Your doing good and are above average. Focus on your weaknesses and build up your strengths. Practice HOTS.\n")
    if 10<= Math_rel < 20:
        print("      Your an above average student and have the potential to score much better. Start solving materials like RS aggarwal, Rd sharma etc to improve your speed and accuracy.\n")
    if 20 <= Math_rel < 30:
        print("      Your marks are average in Maths wrt to your peers. Start from basics by thoroughly solving NCERT's and NCERT materials like exemplar.\n")
    if 30 <= Math_rel < 40:
        print("      Your marks are average in Maths wrt to your peers. Start from basics by thoroughly solving NCERT's and NCERT materials like exemplar.\n")
    if 40 <= Math_rel < 50:
        print("      Your marks are average in Maths wrt to your peers. Start from basics by thoroughly solving NCERT's and NCERT materials like exemplar.\n")
    if 50 <= Math_rel < 60:
        print("      Your marks are average in Maths wrt to your peers. Start from basics by thoroughly solving NCERT's and NCERT materials like exemplar.\n")
    if 60 <= Math_rel < 70:
        print("      Your marks are average in Maths wrt to your peers. Start from basics by thoroughly solving NCERT's and NCERT materials like exemplar.\n")

    print("   English:")


    if Eng_rel<5:
        print("     Your hard work payed off. Your very close of becoming topper of your class.Keep your way of studying the same.\n")
    if 5 <= Eng_rel < 10:
        print("     Your doing good and are above average. Focus on your weaknesses and build up your strengths. Practice HOTS.\n")
    if 10 <= Eng_rel < 20:
        print("     Your an above average student and have the potential to score much better. Start solving materials like RS aggarwal, Rd sharma etc to improve your speed and accuracy.\n")
    if 20 <= Eng_rel < 30:
        print("     Your marks are average in Maths wrt to your peers. Start from basics by thoroughly solving NCERT's and NCERT materials like exemplar.\n")
    if 30 <= Eng_rel < 40:
        print("     Your marks are average in Maths wrt to your peers. Start from basics by thoroughly solving NCERT's and NCERT materials like exemplar.\n")
    if 40 <= Eng_rel < 50:
        print("     Your marks are average in Maths wrt to your peers. Start from basics by thoroughly solving NCERT's and NCERT materials like exemplar.\n")
    if 50 <= Eng_rel < 60:
        print("     Your marks are average in Maths wrt to your peers. Start from basics by thoroughly solving NCERT's and NCERT materials like exemplar.\n")
    if 60 <= Eng_rel < 70:
        print("      Your marks are average in Maths wrt to your peers. Start from basics by thoroughly solving NCERT's and NCERT materials like exemplar.\n")

    print("   Physics:")
    if Phy_rel<5:
        print("    Your hard work payed off. Your very close of becoming topper of your class.Keep your way of studying the same.\n")
    if 5 <= Phy_rel < 10:
        print("    Your doing good and are above average. Focus on your weaknesses and build up your strengths. Practice HOTS.\n")
    if 10 <= Phy_rel < 20:
        print("    Your an above average student and have the potential to score much better. Start solving materials like RS aggarwal, Rd sharma etc to improve your speed and accuracy.\n")
    if 20 <= Phy_rel < 30:
        print("    Your marks are average in Maths wrt to your peers. Start from basics by thoroughly solving NCERT's and NCERT materials like exemplar.\n")
    if 30 <= Phy_rel < 40:
        print("    Your marks are average in Maths wrt to your peers. Start from basics by thoroughly solving NCERT's and NCERT materials like exemplar.\n")
    if 40 <= Phy_rel < 50:
        print("    Your marks are average in Maths wrt to your peers. Start from basics by thoroughly solving NCERT's and NCERT materials like exemplar.\n")
    if 50 <= Phy_rel < 60:
        print("    Your marks are average in Maths wrt to your peers. Start from basics by thoroughly solving NCERT's and NCERT materials like exemplar.\n")
    if 60 <= Phy_rel < 70:
        print("    Your marks are average in Maths wrt to your peers. Start from basics by thoroughly solving NCERT's and NCERT materials like exemplar.\n")

    print("   Chemistry:")
    if Chem_rel<5:
        print("    Your hard work payed off. Your very close of becoming topper of your class.Keep your way of studying the same.\n")
    if 5 <= Chem_rel < 10:
        print("    Your doing good and are above average. Focus on your weaknesses and build up your strengths. Practice HOTS.\n")
    if 10 <= Chem_rel < 20:
        print("    Your an above average student and have the potential to score much better. Start solving materials like RS aggarwal, Rd sharma etc to improve your speed and accuracy.\n")
    if 20 <= Chem_rel < 30:
        print("    Your marks are average in Maths wrt to your peers. Start from basics by thoroughly solving NCERT's and NCERT materials like exemplar.\n")
    if 30 <= Chem_rel < 40:
        print("    Your marks are average in Maths wrt to your peers. Start from basics by thoroughly solving NCERT's and NCERT materials like exemplar.\n")
    if 40 <= Chem_rel < 50:
        print("    Your marks are average in Maths wrt to your peers. Start from basics by thoroughly solving NCERT's and NCERT materials like exemplar.\n")
    if 50 <= Chem_rel < 60:
        print("    Your marks are average in Maths wrt to your peers. Start from basics by thoroughly solving NCERT's and NCERT materials like exemplar.\n")
    if 60 <= Chem_rel < 70:
        print("    Your marks are average in Maths wrt to your peers. Start from basics by thoroughly solving NCERT's and NCERT materials like exemplar.\n")

    print("   Computer:")
    if Comp_rel<5:
        print("     Your hard work payed off. Your very close of becoming topper of your class.Keep your way of studying the same.\n")
    if 5 <= Comp_rel < 10:
        print("     Your doing good and are above average. Focus on your weaknesses and build up your strengths. Practice HOTS.\n")
    if 10 <= Comp_rel < 20:
        print("     Your an above average student and have the potential to score much better. Start solving materials like RS aggarwal, Rd sharma etc to improve your speed and accuracy.\n")
    if 20 <= Comp_rel < 30:
        print("     Your marks are average in Maths wrt to your peers. Start from basics by thoroughly solving NCERT's and NCERT materials like exemplar.\n")
    if 30 <= Comp_rel < 40:
        print("     Your marks are average in Maths wrt to your peers. Start from basics by thoroughly solving NCERT's and NCERT materials like exemplar.\n")
    if 40 <= Comp_rel < 50:
        print("     Your marks are average in Maths wrt to your peers. Start from basics by thoroughly solving NCERT's and NCERT materials like exemplar.\n")
    if 50 <= Comp_rel < 60:
        print("     Your marks are average in Maths wrt to your peers. Start from basics by thoroughly solving NCERT's and NCERT materials like exemplar.\n")
    if 60 <= Comp_rel < 70:
        print("     Your marks are average in Maths wrt to your peers. Start from basics by thoroughly solving NCERT's and NCERT materials like exemplar.\n")


