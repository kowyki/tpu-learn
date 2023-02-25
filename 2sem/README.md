| # | Статус |
| ------ | ------ |
| 01 | Решено |
| 02 | ... |
| 03 | ... |
| 04 | Решено |
| 05 | Решено |
| 06 | Решено |
| 07 | ... |
| 08 | Решено |
| 09 | ... |
| 10 | Решено |
| 11 | ... |
| 12 | ... |
| 13 | ... |
| 14 | ... |
| 15 | ... |
| 16 | ... |
| 17 | ... |
| 18 | ... |
| 19 | Решено |
| 20 | Решено |
| 21 | Решено |
| 22 | ... |
| 23 | Решено |
| 24 | Решено |
| 25 | Решено |
| 26 | Решено |
| 27 | ... |

### Алортимы решения

#### №5

1. Организуем перебор
2. Перевод числа в двоичную систему
3. Дописываем и заменяем по условию задачи
4. Перевод в дестяичную систему и проверка условия

```python
for N in range(516):
    b = f'{N:b}'

    if N % 2 == 0: 
        b += '10'
    else:
        b = '1' + b + '01'
    
    if int(b, 2) > 516:
        print(b)
        break
```

#### №6

1. Вспомнить команды черепашки
2. Нарисовать по алгоритму
3. Подняв перо, нарисовать точки
4. Посчитать точки

```python
from turtle import *

left(90)

for i in range(7):
    forward(300)
    right(120)

pu()

for x in range(1,9):
    for y in range(1,10):
        goto(x*30,y*30)
        dot(5)
done()
```

#### №8

1. Генерацмия всех возможных вариантов (for/product)
2. В зависимости от условия прверяем строчку на условия
3. Выводим счётчик значений

```python
from itertools import product
nums = product('01234567', repeat = 5)
k = 0
n1 = '16 36 56 76 61 63 65 67'
n2 = n1.split()
for n1 in nums:
    b = ''.join(n1)
    s = []
    if b.count('6') == 1 and b[0] != '0':
        for x in n2:
            if x in b:
                s.append(x)
        if not s: 
            k+=1
print(k)
```

#### № 14

1. 
2. 
3.
4. 

```python
a = '0123456789abcde'

for x in a:
    f = int(f'123{x}5', 15) + int(f'1{x}233', 15)
    if f % 14 == 0:
        print(f // 14, x)
        break
```

#### №19-21

1. Расписать через простой граф
2. Выбрать минимальное значение
3. Рассматриваем позицию после 1 хода (2 варианта)
4. Расписываем минимальное и максимальное действия
5. Расписываем максимальный ход Пети через минимальный ход Вани



#### №23
1. С помощью product создаём объект со всеми комбинациями искомой строки
2. Перебор программ в с совокупности программ
3. Переводим начальное значение в исходное положение
4. Используем команду для пропуска итерации неподходящих программ
5. Заходим в программу и анализируем команды
6. Выходим из одного цикла и переходим к следующей программе


#### №24
```python
with open('24.txt') as f:
    s = f.readline().replace('C','S').replace('D','S').replace('F','S')
    s = s.replace('A','G').replace('O','G')
    s = s.replace('SG','*')
    k = kmax = 0
    for i in s:
        if i == '*'
            k += 1
            kmax = max(k,kmax)
        else: k = 0
print(kmax)
```

#### №25
```python

from operator import itemgetter
def func25(num):
    if int(num) % 2023 == 0:
        t = int(num) // 2023
        ig.append(num)
        igt.append(t)

ig = []
igt = []

for i in range(10):
  for y in range(1000000):
      num = '1' + str(i) + '21394'
      func25(num)

      num = '1' + str(i) + '2139' + str(y) + '4'
      if int(num) > 10**10: break
      func25()

ig1 = list(zip(ig, igt))
print(*ig1)
print(sorted(ig1, key = itemgetter(1)))
for i in range(2023, 10**10, 2023):
    num = str(i)
    if num[0] == '1' and num[2:6] == '2139' and num[-1] == '4':
        print(i, i // 2023)


```


#### №26
```python
with open('26.txt') as f:
    data = [int(x) for x in f]
    s = sorted(s[1:], reverse = True)
    k, m = 1, s[0]

    for i in range(1, len(s)):
        if s[i] + 3 <= m:
            m = s[i]
            k += 1
print(k, m)

```













