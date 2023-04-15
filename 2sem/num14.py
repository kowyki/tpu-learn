# Demo-2022
def d22():
    a = 3*16**2018 - 2*8**1028 - 3*4**1100 - 2**1050 - 2022
    b = 0

    while a > 0:
        b += a % 4 == 3
        a = a // 4

    print(b)

# Demo-2023
def d23():
    a = '0123456789abcde'

    for x in a:
        f = int(f'123{x}5', 15) + int(f'1{x}233', 15)
        if f % 14 == 0:
            print(f // 14, x)
            break

d23()