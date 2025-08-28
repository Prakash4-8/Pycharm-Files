text = open('C:/Users/bablu/PycharmProjects/PythonFundamentalSpringBoard/blankfile', 'r+')
print(text.tell())
for i in range(11):
    text.write(str(i)+10*' ')
    text.write('\n')
text.write('The end')
text.seek(0)
text.write('the start')
print(text.tell())
