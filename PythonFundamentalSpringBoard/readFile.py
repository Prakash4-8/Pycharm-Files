# file.open() to open the file
# file.read() to loads the entire file into memory
# file.readline() to reads a single line from the file into memory
# file.readlines() to read all of the lines of a file into list
# file.write() to writes output to the file
# file.seek() to move the file object postion to a certain location in the file
text = open('C:/Users/bablu/PycharmProjects/PythonFundamentalSpringBoard/sample1.txt', 'r', encoding='utf-8')
text = text.readlines()
print(text)
"""sentences = text.split('.')
for sentence in sentences:
    if 'machine learning' in sentence:
        print(sentence)
"""
