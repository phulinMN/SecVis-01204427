import datetime
import json

all_time = {}
user_time = {}
arr_lines = []
with open('login_timestamp.txt') as f:
    arr_lines = f.readlines()

def convert_time(unix_time):
    date = []
    time = int(unix_time)/1000.00

    day = datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d')
    time = datetime.datetime.fromtimestamp(time).strftime('%H:%M:%S')
    date = [day, time]
    return date

def gen_time():
    x = 0
    for i in range(96):
        all_time[x] = 0
        x += 15

def interval_time(start,end):
    s = int(start[1].split(':')[0])*60 + int(start[1].split(':')[1])
    e = int(end[1].split(':')[0])*60 + int(end[1].split(':')[1])
    for i in all_time:
        if s >= i and e < i:
            all_time[i] += 1

gen_time()
for i in arr_lines:
    i = i.replace('\n', '').split(' ')
    if i[2] != '-':
        login = convert_time(i[1])
        logout = convert_time(i[2])
        user_time[i[0]] = {
            "time_login": login,
            "time_logout": logout
        }
        interval_time(login,logout)
# print(all_time)
data = []
for i in all_time:
    x = int(i/60)
    y = i%60
    if x < 10:
        x = '0' + str(x)
    if y < 10:
        y = '0' + str(y)
    t = str(x) + ':' + str(y)
    # print(t)
    item = []
    item.append(t)
    item.append(all_time[i])
    data.append(item)
# print(data)

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
