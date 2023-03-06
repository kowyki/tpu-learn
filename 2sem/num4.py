# Easy EGE

def ezege():
    from itertools import product

    N = 12

    for x in range(2,6):
        b = product('12', repeat = x)
        for i in b:
            prog = ''.join(i)
            for n in prog:
                if n == '1': N -= 1
                if n == '2': N *= 7
                if N == 489: 
                    print(N)
                    break
        # N = 12

def d23():
    from itertools import product

    N = 1

    for x in range(6, 35):
        b = product('12', repeat = x)
        for i in b:
            prog = ''.join(i)
        print(x)

d23()