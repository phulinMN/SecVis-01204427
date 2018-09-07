import datetime
import json

arr_lines = []

def convert_time(unix_time):
    date = []
    time = int(unix_time)/1000000.00
    time = datetime.datetime.fromtimestamp(time).strftime('%H:%M:%S')
    return time

with open('3_2_data.txt') as f:
    arr_lines = f.readlines()

data = []
t_min = []
r = ''
a = ''
for i in range(60):
    if i < 10:
        r = '0' + str(i)
    else:
        r = str(i)
    t_min.append(r)
# print(t_min)
top_username = []
username = {}
ip_src = {}
ip_dst = {}
port_dst = {}
host = {}
for i in arr_lines:
    i = i.replace('\n', '')
    i = i.split(' ')
    if i[1] not in username:
        username[i[1]] = 0
    else:
        username[i[1]] += 1

sort_user = sorted(username.values(), reverse=True)
for i in username:
    for x in range(10):
        if username[i] == sort_user[x]:
            top_username.append(i)
print(top_username)

for i in arr_lines:
    i = i.replace('\n', '')
    i = i.split(' ')
    a = convert_time(i[0])
    a = a.split(':')[2]
    if i[1] in top_username:
        if i[2] not in ip_src:
            ip_src[i[2]] = 0
        else:
            ip_src[i[2]] += 1
        if i[3] not in ip_dst:
            ip_dst[i[3]] = 0
        else:
            ip_dst[i[3]] += 1
        if i[4] not in port_dst:
            port_dst[i[4]] = 0
        else:
            port_dst[i[4]] += 1
        if i[5] not in host:
            host[i[5]] = 0
        else:
            host[i[5]] += 1
        data.append([a, i[1], i[2], i[3], i[4], i[5]])
print(sorted(ip_src.keys()))
print(sorted(ip_dst.keys()))
print(sorted(port_dst.keys()))
print(sorted(host.keys()))
print(t_min)

with open('parallel.json', 'w') as outfile:
    json.dump(data, outfile)