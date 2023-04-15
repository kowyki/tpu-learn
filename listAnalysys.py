ls = [20, 2, 5, 0, 8, 10, 12, 5]

for i in range(len(ls) - 1):
    for k in range(len(ls) - 1 - i):
        if ls[k] > ls[k+1]:
            ls[k], ls[k+1] = ls[k+1], ls[k]
print(ls)