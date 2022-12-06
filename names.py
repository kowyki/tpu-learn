from random import *
import random

consonants = ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ']
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

for i in range(randint(1, len(mainOrder))):
    Name[mainOrder[randint(0, (len(mainOrder))-1)]] = random.choice(consonants)

for i in range(nameLen):
    endName += Name[i]

print(endName)
