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
username = []
ip_src = []
ip_dst = []
port_dst = []
host = []
for i in arr_lines:
    i = i.replace('\n', '')
    i = i.split(' ')
    a = convert_time(i[0])
    a = a.split(':')[2]
    data.append([a, i[1], i[2], i[3], i[4], i[5]])
    if i[1] not in username:
        username.append(i[1])
    if i[2] not in ip_src:
        ip_src.append(i[2])
    if i[3] not in ip_dst:
        ip_dst.append(i[3])
    if i[4] not in port_dst:
        port_dst.append(i[4])
    if i[5] not in host:
        host.append(i[5])
print(host)

with open('parallel.json', 'w') as outfile:
    json.dump(data, outfile)