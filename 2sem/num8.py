# ЕГЭ-8
# №64
def n64():
    # dictionary = 'АБВГД'
    n = 0

    # for a in dictionary:
    #     for b in dictionary:
    #         for c in dictionary:
    #             ...

    n = 5**3
    print(n*2)

# №64 - itertools
def n64i():
    from itertools import product

    n = 0
    p = product('ШКОЛА', repeat = 3)
    for x in p:
        if x.count('К') == 1:
            n += 1
    print(n)

# №хх - itertools
def nXXi():
    from itertools import product

    n = 0
    p = product('АБВГДЯ', repeat = 4)

    for a in p:
        if a.count('Я') == 1 and (a[0] == 'Я' or a[-1] == 'Я'):
            n += 1
    print(n)


# №70
def n70():
    dictionary = 'АБВ'
    n = 0

    for a in dictionary:
        for b in dictionary:
            for c in dictionary:
                for d in dictionary:
                    n += 1
                    for c in dictionary:
                        n += 1

    print(n)

#Demo 23
def d23():
    d = '0123'
    for a in d:
        for b in d:
            for c in d:
                print(a+b+c)

#Demo 23 itertools
def d23i():
    from itertools import product
    c1 = []
    k = 0
    p = product('01234567', repeat = 5)
    n1 = '16 36 56 76 61 63 65 67'
    n2 = n1.split()
    for n1 in p:
        b = ''.join(n1)
        s = []
        if b.count('6')==1 and b[0]!='0':
            for x in n1:
                if x in b:
                    s.append(x)
            if not s: 
                k+=1
    k += len(list(s))
    print(k)


    # for i in p:
    #     a = ''.join(i)
    #     c1.append(a)
    # if 
    # print(c1)

# 8 задача: 8-значное число из 6-ричной системы счисления. Найти все строки где есть 4 и она не стоит рядом с чётным числом, сумма цифр числа - чётное число.
# 6 задача: определить количество точек внутри фигуры созданной по программе: прямоугольный равнобедренный треугольник, длина катета = 15, прямой угол в левом верхнем углу, левый катет параллелен 0Y
# 5 задача: найти минимальное N. N в двоичный формат, если число чётное, то справа приписывается 110 вместо последних двух символов. Если нечётное, то вместо последних двух цифр 001, число больше 160.

# 8 задача: 8-значное число из 6-ричной системы счисления. Найти все строки где есть 4 и она не стоит рядом с чётным числом, сумма цифр числа - чётное число.
def test():
    from itertools import product
    nums = product('012345', repeat = 8)
    n1 = '04 24 40 42'
    n2 = n1.split()
    l = 0

    for a in nums:
        c = ''.join(a)
        s = []

        if c.count('4') == 1 and c[0] != '0' and (sum(map(int, list(c))) % 2) == 0:
            for x in n2:
                if x in c:
                    s.append(x)
                if not s:
                    l += 1

    print(l)



def test2():
    a = bin(161)[2:]
    print(a)
    y = '1010001'
    n = int(y, 2)
    

    
    print(n)


test2()