import json

arr_lines = []
with open('user.txt') as f:
    arr_lines = f.readlines()

data = []
for i in arr_lines:
    i = i.replace('\n', '')
    x = i.split(' ')
    x = x[-2:]
    child = {
        'value': x[0],
        'name': x[1]
    }
    data.append(child)
print(data)

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)