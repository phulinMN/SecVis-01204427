import json

arr_lines = []
with open('3_5_egress.txt') as f:
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
    print(x)
    
with open('path_egress.json', 'w') as outfile:
    json.dump(data, outfile)

arr_lines = []
with open('3_6_ingress.txt') as f:
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
    print(x)
    
with open('path_ingress.json', 'w') as outfile:
    json.dump(data, outfile)