import math

q = input('Напиште номер типа задачи: \n1. Выбор неизвестного\n2. Выбор известного\n')

if q == '1':
    A = input(
        'Тип задачи: \n1. Текстовая информация \n2. Звуковая информация \n3. Графическая информация\n')
    match A:
        case '1':
            print('''
I = K * i
N = 2^i
I - Количество информации в сообщении (в битах)
K - Количество символов в сообщении
i - Информационный вес символа (в битах)
N - Мощность алфавита''')

            ans = input('Напишите что необходимо найти I, K, i, N: ')

            match ans:
                case 'I':
                    K = int(input('K = '))
                    i = int(input('i = '))
                    print(f'I = {K * i} бит')

                case 'K':
                    I = int(input('I = '))
                    i = int(input('i = '))
                    print(f'K = {I / i} символов в сообщении')
                case 'i':
                    N = input('N = ')
                    if N == '':
                        I = int(input('I = '))
                        K = int(input('K = '))
                        print(f'i = {I / K} бит')
                    else:
                        print(f'i = {math.log2(int(N))} бит')
                case 'N':
                    i = int(input('i = '))
                    print(f'N = {2**i} символов в алфавите')
        case '2':
            print('''
V = I * M * t * k
V - Объём звукового файла (в битах)
I - Глубина кодирования звука (в битах)
M - Частота дискретизации звука
t - Длительность звучания файла (в секундах)
k - Количество каналов звучания''')
            ans = input('Напишите что необходимо найти V, I, M, t, k: ')

            match ans:
                case 'V':
                    I = int(input('I = '))
                    M = int(input('M = '))
                    t = int(input('t = '))
                    k = int(input('k = '))
                    print(f'V = {I * M * t * k} бит')

                case 'I':
                    V = int(input('V = '))
                    M = int(input('M = '))
                    t = int(input('t = '))
                    k = int(input('k = '))
                    print(f'I = {V / (M * t * k)} бит')

                case 'M':
                    V = int(input('V = '))
                    I = int(input('I = '))
                    t = int(input('t = '))
                    k = int(input('k = '))
                    print(f'M = {V / (I * t * k)} герц')

                case 't':
                    V = int(input('V = '))
                    M = int(input('M = '))
                    I = int(input('I = '))
                    k = int(input('k = '))
                    print(f't = {V / (I * M * k)} секунд')

                case 'k':
                    V = int(input('V = '))
                    M = int(input('M = '))
                    I = int(input('I = '))
                    t = int(input('t = '))
                    print(f'k = {V / (I * M * t)} канала(-а)')
        case '3':
            print('''
I = i * X * Y
I - Информационный объём (в битах)
i - Глубина цвета (в битах)
X - Ширина изображения (в пикселях)
Y - Высота изображения (в пикселях)''')
            ans = input('Напишите что необходимо найти I, i, X, Y: ')

            match ans:
                case 'I':
                    i = int(input('i = '))
                    X = int(input('X = '))
                    Y = int(input('Y = '))
                    print(f'I = {i * X * Y} бит')

                case 'i':
                    I = int(input('I = '))
                    X = int(input('X = '))
                    Y = int(input('Y = '))
                    print(f'i = {I / (X * Y)} бит')

                case 'X':
                    I = int(input('I = '))
                    i = int(input('i = '))
                    Y = int(input('Y = '))
                    print(f'X = {I / (i * Y)} пикселей')

                case 'Y':
                    I = int(input('I = '))
                    i = int(input('i = '))
                    X = int(input('X = '))
                    print(f'Y = {I / (i * X)} пикселей')

if q == '2':
    A = input(
        'Тип задачи: \n1. Текстовая информация \n2. Звуковая информация \n3. Графическая информация\n')
    print('Если значение отсутствует, нажмите Enter')
    match A:
        case '1':
            print('''
I = K * i
N = 2^i
I - Количество информации в сообщении (в битах)
K - Количество символов в сообщении
i - Информационный вес символа (в битах)
N - Мощность алфавита''')
            I = input('I = ')
            K = input('K = ')
            i = input('i = ')
            N = input('N = ')

            if i == '' and I == '' and K == '':
                i = math.log2(int(N))
                print(f'i = {i} бит')

            elif i == '' and N == '':
                i = int(I) / int(K)
                print(f'i = {i} бит')

            if I == '' and K and i:
                print(f'I = {int(K) * int(i)} бит')

            if K == '' and i and I:
                print(f'K = {int(I) / int(i)} символов в сообщении')

            if N == '' and i:
                print(f'N = {2**int(i)} символов в алфавите')
        case '2':
            print('''
V = I * M * t * k
V - Объём звукового файла (в битах)
I - Глубина кодирования звука (в битах)
M - Частота дискретизации звука
t - Длительность звучания файла (в секундах)
k - Количество каналов звучания''')
            V = input('V = ')
            I = input('I = ')
            M = input('M = ')
            t = input('t = ')
            k = input('k = ')

            if V == '':
                print(f'V = {int(I) * int(M) * int(t) * int(k)} бит')

            if I == '':
                print(f'I = {int(V) / (int(M) * int(t) * int(k))} бит')

            if M == '':
                print(f'M = {int(V) / (int(I) * int(t) * int(k))} герц')

            if t == '':
                print(f't = {int(V) / (int(I) * int(M) * int(k))} секунд')

            if k == '':
                print(f'k = {int(V) / (int(I) * int(M) * int(t))} канал(-а)')
        case '3':
            print('''
I = i * X * Y
I - Информационный объём (в битах)
i - Глубина цвета (в битах)
X - Ширина изображения (в пикселях)
Y - Высота изображения (в пикселях)''')
            I = input('I = ')
            i = input('i = ')
            X = input('X = ')
            Y = input('Y = ')

            if I == '':
                print(f'I = {int(i) * int(X) * int(Y)} бит')

            if i == '':
                print(f'i = {int(I) / (int(X) * int(Y))} бит')

            if X == '':
                print(f'X = {int(I) / (int(i) * int(Y))} пикселей')

            if Y == '':
                print(f'Y = {int(I) / (int(i) * int(X))} пикселей')

input()
