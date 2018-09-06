import json

arr_lines = []
with open('egress_path.txt') as f:
    arr_lines = f.readlines()

data = []
for i in arr_lines:
    i = i.replace('\n', '')
    i = i.split(' ')
    data.append(i[1])
# print(data)
count = 0
unknown = 0
ftype = {}
check = 0
for i in data:
    check = 0
    i = i.split('.')
    if len(i) > 1:
        for x in ftype:
            if x == i[len(i)-1]:
                ftype[x] += 1
                check = 1
        if check == 0:
            ftype[i[len(i)-1]] = 0
        # print(ftype)
    else:
        unknown += 1
# print(count)
print(unknown)
print(ftype)

# for x in ftype:
#     print(x)
#     print(ftype[x])