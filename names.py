from random import *
import random

consonants = ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ']
sufW = ["она", "еньк", "ишк", "иньк", "оньк", "ечк", "инк"]
sufM = ["он", "ик", "ек", "ен", "ок", "нок", "ник", "вик"]

def mainP():
    mainOrder = []
    k = 0
    endName = ''

    inputName = (input('Введите имя: '))
    Name = list(inputName.upper())
    nameLen = len(Name)

    for i in Name:
        for c in consonants:
            if i == c:
                mainOrder.append(k)
        k += 1

    if mainOrder == []:
        print('Изменение невозможно')
        input()
        quit()

    for i in range(randint(1, len(mainOrder))):
        Name[mainOrder[randint(0, (len(mainOrder))-1)]] = random.choice(consonants)

    for i in range(nameLen):
        endName += Name[i]

    print(endName)

def authors():
     print('Разработчик алгоритма замены: Никитин Павел')
     print('Разработчик-конструктор: Тимур Бакеев')
     print('Разработчик алгоритма добавления окончаний: Вячеслав Воронин')
     print('Тестировщик: Максим Вайс')
     print('Программист-консультант: Кирилл Малахов')

while True:
    ans = int(input('1. Изменить имя \n2. Авторы \n3. Выйти'))
    if ans == 1:
        mainP()
    if ans == 2:
        authors()
    if ans == 3:
        quit()

import random




    
while True:
    print("Введите свое имя: ")
    name = input()
    print("Введите свой гендер (муж, жен): ")
    gen = input()
    res = newName(name) + Suf(gen)
