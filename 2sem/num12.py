# Demo-22
def d22():
    a = '8'*86
    n1 = '1111'
    n2 = '8888'

    while n1 in a or n2 in a:
        if n1 in a:
            a = a.replace('1111', '8', 1)
        else:
            a = a.replace('8888', '11', 1)

    print(a)

# Demo-23
def d23():
    LS = []

    for n in range(1, 10000):
        ch = []
        nsqrt = int(n**0.5)
        
        for i in range(2, nsqrt+1):
            if n % i == 0:
                ch.append(n)
        if not ch:
            LS.append(n)  

    for n in range(1, 10):
        if (39*3 + 4*n) in LS:
            print(n)
            break