import csv

with open("C:/Users/bablu/Desktop/Data Set/AP - Sheet1.csv", 'r+') as f:
    mock_data_reader = csv.reader(f)
    line_count = 1
    users = []
    for row in mock_data_reader:
        if line_count > 1:
            Transaction1 = row[1]
            Transaction2 = row[2]
            users.append({'Transaction 1': row[1], 'Transaction 1': row[2]})
        line_count += 1
for user in users:
    print(user)
