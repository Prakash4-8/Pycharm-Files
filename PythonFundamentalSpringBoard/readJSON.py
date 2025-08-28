import json
with open('unece.json') as f:
    data = json.loads(f.read())
print(data)
print(type(data))