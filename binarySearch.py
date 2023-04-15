import random as rand

numList = []
p = 0
flag = 1

for i in range(0, rand.randint(10, 100)):
    p += rand.randint(1, 7)
    numList.append(p)

ln = len(numList) % 2
ind = len(numList) // 2

print(numList)

for i in range(10):
    match ln:
        case 1:
            ind = ind // 2
        case 0:
            ind = (ind // 2) + 1

    if (numList[ind] < numList[ind+1]) and ind != 0:
        ind //= 2
    if ind == 0:
        flag = 0

print(numList[ind])