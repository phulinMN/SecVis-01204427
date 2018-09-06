import datetime
import json

count = {}
arr_lines = []
ipv4 = []
ipv6 = []
dual = []
with open('ip_time.txt') as f:
    arr_lines = f.readlines()

def convert_time(unix_time):
    time = int(unix_time)/1000.00
    time = datetime.datetime.fromtimestamp(time).strftime('%H:%M:%S')
    return time

def gen_time():
    x = 0
    for i in range(96):
        count[x] = 0
        x += 15

def calculate_time(start, end):
    s = int(start.split(':')[0])*60 + int(start.split(':')[1])
    e = int(end.split(':')[0])*60 + int(end.split(':')[1])
    for i in count:
        if s >= i and e < i:
            count[i] += 1

gen_time()
for i in arr_lines:
    i = i.replace('\n', '').split(' ')
    if i[1] != '-':
        child = {
            "login": convert_time(i[0]),
            "logout": convert_time(i[1])
        }
        # if i[2] != '-' and i[3] == '-':
        #     ipv4.append(child)
        #     calculate_time(convert_time(i[0]), convert_time(i[1]))
        # if i[2] == '-' and i[3] != '-':
        #     ipv6.append(child)
        #     calculate_time(convert_time(i[0]), convert_time(i[1]))
        if i[2] != '-' and i[3] != '-':
            dual.append(child)
            calculate_time(convert_time(i[0]), convert_time(i[1]))
# print(count)
ans = {}
a = []
for i in count:
    x = int(i/60)
    y = i%60
    if x < 10:
        x = '0' + str(x)
    if y < 10:
        y = '0' + str(y)
    t = str(x) + ':' + str(y)
    ans[t] = count[i]
    a.append(count[i])
    print(t)
print(a)

