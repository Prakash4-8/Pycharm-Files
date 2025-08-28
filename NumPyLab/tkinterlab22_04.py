from matplotlib import pyplot as plt
lbl = ['Sub1', 'Sub2', 'Sub3','Sub4', 'Sub5']
marks = [65, 75, 85, 80, 72]
xpld = (0, 0, 0, 0, 0)
plt.pie(marks, explode= xpld, labels=lbl, autopct='%1f%%', shadow=True, startangle=45)
plt.axis('Equal')
plt.title('marks pie chart')
plt.show()