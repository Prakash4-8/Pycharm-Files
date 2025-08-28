import json
userInfo = { "Name": "Prakash","Age": 21, "Occupation": "Student", "Contact":7655045712}
with open('exampleWrite.json', 'r+') as f:
    json.dump(userInfo, f)