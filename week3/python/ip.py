from datetime import datetime

fn = open('login-20170102-anon.csv.txt', 'r')

data = {}

for line in fn:
    x = line.split(' ')
    t = 0
    if x[5] != '-' and x[6] != '-':
        t = 2
    elif x[5] != '-' and x[6] == '-':
        t = 4
    elif x[5] == '-' and x[6] != '-':
        t = 6

    if x[1] != '-' and x[3] != '-':
        if x[0] in data:
            data[x[0]].append(t)
            data[x[0]].append(x[1])
            data[x[0]].append(x[3])
        else:
            data[x[0]] = [t, x[1], x[3]]

b2 = [0] * 1440
b4 = [0] * 1440
b6 = [0] * 1440

for i in data:
    temp = data[i]
    st = int(temp[1])/1000.0
    h = datetime.fromtimestamp(st).strftime('%H')
    m = datetime.fromtimestamp(st).strftime('%M')
    st = int(h)*60 + int(m)
    
    ed = int(temp[2])/1000.0
    h = datetime.fromtimestamp(ed).strftime('%H')
    m = datetime.fromtimestamp(ed).strftime('%M')
    ed = int(h)*60 + int(m)

    for j in range(st, ed + 1):
        if temp[0] == 2:
            b2[j] += 1
        elif temp[0] == 4:
            b4[j] += 1
        elif temp[0] == 6:
            b6[j] += 1

y = []
x2 = []
x4 = []
x6 = []

for i in range(0, 1440, 15):
    x = str(int(i/60)).zfill(2) + ':' + str(i%60).zfill(2)
    sum2 = 0
    sum4 = 0
    sum6 = 0
    for j in range(i, i + 15):
        sum2 += b2[j]
        sum4 += b4[j]
        sum6 += b6[j]

    y.append(x)
    x2.append(sum2)    
    x4.append(sum4)    
    x6.append(sum6)    
    
print(y)
print(x2)
print(x4)
print(x6)