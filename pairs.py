numList = [0, 1, 2, 3, 4]
a = 0

f = []

for i in range(len(numList)):
    for k in range(len(numList) - i):
        if (numList[i] * numList[i+k]) % 2 == 0:
            f.append([numList[i], numList[i+k]])

print(f)

for i in range(len(f)):
    if f[i-a][0] == f[i-a][1]:
        f.pop(i-a)
        a += 1

print(len(f))