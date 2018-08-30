import datetime
import json


all_time = {}
interval = {}
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
    for i in range(24):
        if i < 10:
            k = '0' + str(i) + ':00'
            all_time[k] = 0
            k = '0' + str(i) + ':15'
            all_time[k] = 0
            k = '0' + str(i) + ':30'
            all_time[k] = 0
            k = '0' + str(i) + ':45'
            all_time[k] = 0
        else:
            k = str(i) + ':00'
            all_time[k] = 0
            k = str(i) + ':15'
            all_time[k] = 0
            k = str(i) + ':30'
            all_time[k] = 0
            k = str(i) + ':45'
            all_time[k] = 0
    # a = []
    # for i in all_time:
    #     a.append(i)
    # print(a)

def interval_time(start):
    s = start[1].split(':')
    for i in all_time:
        # print(i)
        h_start = int(i.split(':')[0])
        h_end = int(i.split(':')[0]) + 1
        if int(s[0]) >= h_start and int(s[0]) < h_end:
            if(int(s[1]) >= int(i.split(':')[1]) and int(s[1]) < int(i.split(':')[0])+15):
                all_time[i] += 1

gen_time()
for i in arr_lines:
    i = i.replace('\n', '').split(' ')
    if i[2] != '-':
        login = convert_time(i[1])
        interval_time(login)
        # print(login[1])
        # interval[login] = 0
login = all_time

gen_time()
for i in arr_lines:
    i = i.replace('\n', '').split(' ')
    if i[2] != '-':
        logout = convert_time(i[2])
        interval_time(logout)
        # print(login[1])
        # interval[login] = 0
logout = all_time
a = []
for i in logout:
    a.append(logout[i])
print(a)
# print(logout)