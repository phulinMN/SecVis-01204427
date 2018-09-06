import json

arr_lines = []
with open('egress_hostname.txt') as f:
    arr_lines = f.readlines()
data = []

for i in arr_lines:
    i = i.replace('\n', '')
    x = i.split(' ')
    x = x[-3:]
    child = {
        'value': x[0],
        'name': x[2]
    }
    data.append(child)
print(data)
    
with open('egress_hostname.json', 'w') as outfile:
    json.dump(data, outfile)