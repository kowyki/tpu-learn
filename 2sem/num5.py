for N in range(516):
    b = f'{N:b}'

    if N % 2 == 0: 
        b += '10'
    else:
        b = '1' + b + '01'
    
    if int(b, 2) > 516:
        print(b)
        break