import json

arr_lines = []
with open('user.txt') as f:
    arr_lines = f.readlines()

data = []
list_data = {}
for i in arr_lines:
    i = i.replace('\n', '')
    x = i.split(' ')
    x = x[-2:]
    list_data[x[1]] = int(x[0])
sort_user = sorted(list_data, key=list_data.__getitem__, reverse=True)
sort_value = sorted(list_data.values(), reverse=True)

for i in range(len(sort_user)):
    print(i)
    child = {
        'value': sort_value[i],
        'name': sort_user[i]
    }
    data.append(child)

print(data)

with open('user_request.json', 'w') as outfile:
    json.dump(data, outfile)