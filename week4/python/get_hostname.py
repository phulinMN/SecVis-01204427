import json

arr_lines = []
arr_lines2 = []
with open('egress_hostname.txt') as f:
    arr_lines = f.readlines()
# with open('ingress_hostname.txt') as f:
#     arr_lines2 = f.readlines()
data = []
# data2 = []

for i in arr_lines:
    i = i.replace('\n', '')
    x = i.split(' ')
    x = x[-2:]
    print(x)
    child = {
        'value': int(x[0]),
        'name': x[1]
    }
    data.append(child)
print(data)

# for i in arr_lines2:
#     i = i.replace('\n', '')
#     x = i.split(' ')
#     x = x[-3:]
#     child = {
#         'value': x[0],
#         'name': x[2]
#     }
#     data2.append(child)
# print(data2)
    
with open('e_hostname.json', 'w') as outfile:
    json.dump(data, outfile)
# with open('ingress_hostname.json', 'w') as outfile:
#     json.dump(data2, outfile)