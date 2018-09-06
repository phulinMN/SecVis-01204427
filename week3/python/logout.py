from datetime import datetime

fn = open('login-20170102-anon.csv.txt', 'r')

#### logout ####
dict_data = {}
data = []

for line in fn:
    x = line.split(' ')
    if x[3] != '-':
        if x[0] in dict_data:
            dict_data[x[0]].add(x[3])
        else:
            dict_data[x[0]] = set([x[3]])

basket = [0]*1440

for i in dict_data:
    xx = str(dict_data[i])[2:-2]
    s = int(xx)/1000.0
    x = datetime.fromtimestamp(s).strftime('%Y-%m-%d')
    if x == '2017-01-02':
        h = datetime.fromtimestamp(s).strftime('%H')
        m = datetime.fromtimestamp(s).strftime('%M')
        st = int(h)*60 + int(m)
        basket[st] += 1

dataout = []

for i in range(0, 1440, 15):
    x = str(int(i/60)).zfill(2) + ':' + str(i%60).zfill(2)
    summ = 0
    for j in range(i, i + 15):
        summ += basket[j]
    dataout.append([x, summ])

y = []
x = []

for i in dataout:
    y.append(i[0])
    x.append(i[1])

print(y)
print(x)