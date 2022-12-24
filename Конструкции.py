def endWhile():
    while True:
        print('Бесконечный цикл')
        break

def For():
    for x in range(2):
        for y in range(2):
            print(x, y)

def A():
    a = input('Введите значение А: ')
    if a != 2:
        print('a ≠ 2')
    else:
        print('a = 2')

def Flag():
    flag = True
    print(f'Значение флага: {flag}')
    flag = False
    print(f'Значение флага: {flag}')

def If():
    x = input('Введите значение X: ')
    y = input('Введите значение Y: ')
    z = input('Введите значение Z: ')
    if ((y <= x) or not (z)) == False:
        print('False')
    if ((y <= x) or not (z)):
        print('True')

def Perc():
    a = input('Введите значение А: ')
    b = input('Введите значение B: ')
    print(f'Остаток от деления {a} на {b} = {a%b}')
    print(f'Целая часть от деления {a} на {b} = {a//b}')

def List():
    l = input('Введите целочисленные значения списка через пробел \n').split()
    l = list(map(int, l))

    print(l)
    print(bin(2387563247928637592643)[2:])
    print(l.count('1'))
    # print(l.index(2))
    print(l.append(1))
    print(l.sort(reverse=True))
    print(max(l))
    print(min(l))
    print(sum(l))

def txt():
    with open('122.txt') as f:
        numbers=[int(x) for x in f]
        print(numbers[10])

txt()