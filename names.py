from random import *
import random

# Объявление главных переменных
consonants = ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'К', 'Л','М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ч', 'Ш']
sufW = ['она', 'еньк', 'ишк', 'иньк', 'оньк', 'ечк', 'инк', 'ая', 'ия', 'я']
sufM = ['он', 'ик', 'ек', 'ен', 'ок', 'нок', 'ник', 'вик']
pers = ['гипо', 'ано', 'супер', 'сверх', 'купер', 'убер', 'квадра', 'кристи', 'квекто', 'хладо', 'кветта', 'ронта', 'хант', 'соло', 'зе', 'ке', 'еже', 'хроно', 'ра', 'ве', 'за', 'ли', 'жи', 'пе', 'авто', 'мудро', 'дубо', 'славо', 'клее', 'христо', 'мусли', 'кресто', 'ари', 'храмо', 'дур', 'яд', 'яз', 'астро', 'паро', 'водо', 'огне', 'эхо', 'дву', 'ед', 'три', 'шумо', 'рас', 'дис', 'ир', 'до', 'ил', 'ан', 'книго', 'солнце', 'яро', 'ветро', 'аллахо']

# Начало программы
def start():
    inputName = input('Введите имя (чтобы выйти нажмите Enter): ')
    if inputName == '':
        quit()

    randSuf = input('Введите пол (М, Ж): ').upper()

    res = random.choice(pers) + mainP(inputName).lower() + Suf(randSuf)
    print(f'{res.title()}\n')

# Алгоритм преобразования имени
def mainP(inputName):
    mainOrder = []
    k = 0
    endName = ''

    Name = list(inputName.upper())
    nameLen = len(Name)

    for i in Name:
        for c in consonants:
            if i == c:
                mainOrder.append(k)
        k += 1

    if mainOrder == []:
        print('Изменение невозможно')
        start()

    for i in range(randint(1, len(mainOrder))):
        Name[mainOrder[randint(0, (len(mainOrder))-1)]] = random.choice(consonants)

    for i in range(nameLen):
        endName += Name[i]

    return endName

# Добавление случайного суффикса в конце слова
def Suf(randSuf):
    if randSuf[0] == 'М':
        return random.choice(sufM)
    if randSuf[0] == 'Ж':
        return random.choice(sufW)

# Авторы
def authors():
    print('Разработчик алгоритма замены: Никитин Павел')
    print('Разработчик-конструктор: Тимур Бакеев')
    print('Разработчик алгоритма добавления окончаний: Вячеслав Воронин')
    print('Тестировщик: Максим Вайс')
    print('Программист-консультант: Кирилл Малахов')

# Начало программы
st = input('1. Посмотреть авторов \n2. Пропустить \n')
if st == '':
    quit()
if int(st) == 1:
    authors()

while True:
    start()
