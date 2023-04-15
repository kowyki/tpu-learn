import random as rand

numList = []
p = 0
flag = 1

for i in range(0, rand.randint(10, 100)):
    p += rand.randint(1, 7)
    numList.append(p)

mid = len(numList) // 2

while mid > 0:
    if numList[mid] < numList[mid + 1]:
        mid //= 2
        print(numList[mid])

    else:
        print(numList[mid])
        break