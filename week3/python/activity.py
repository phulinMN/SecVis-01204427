arr_lines = []
with open('activity.txt') as f:
    arr_lines = f.readlines()
count = [0,0,0,0]
count = {
    "login-page": 0,
    "RE-LOGIN": 0,
    "TIMEOUT": 0,
    "logout-page": 0
}
for i in arr_lines:
    i = i.replace('\n', '')
    if i == "login-page":
        count["login-page"] += 1
    elif i == "RE-LOGIN":
        count["RE-LOGIN"] += 1
    elif i == "TIMEOUT":
        count["TIMEOUT"] += 1
    elif i == "logout-page":
        count["logout-page"] += 1

print(count)