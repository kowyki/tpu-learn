# Demo-23
def d23():
    for A in range(1, 100000):
        if all(((x % 2 == 0) <= (x % 3 != 0)) or (x + A >= 100) for x in range(1, 100)):
            print(A)
            break

