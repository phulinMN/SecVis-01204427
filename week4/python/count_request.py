import json

arr_lines = []
with open('count_request.txt') as f:
    arr_lines = f.readlines()
count = []
data = []
r = 0
c = ''

graph = []
for i in arr_lines:
    i = i.replace('\n', '')
    x = i.split(' ')
    x = x[-2:]
    if r < 10:
        c = '0' + str(r)
    else:
        c = str(r)
    time = '03:'+ c
    count.append(x[0])
    data.append(time)
    graph.append([time,int(x[0])])
    r += 1
with open('count_request.json', 'w') as outfile:
    json.dump(graph, outfile)