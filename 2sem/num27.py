with open('27-A.txt', 'r') as f:
    a = [int(x) for x in f]
    a.pop(0)

    cost = 0
    cost2 = 0
    
    if len(a) % 2 == 0:
        s =  int(len(a) / 2)

        for t in range(20):
            for i in range(s):
                cost += a[i+t]*i
                
            for i in range(a, 2*a):
                cost += a[i+t]*s
                s -= 1

            if t == 0:
                cost2 = cost

            if t != 0 and (cost < cost2):
                cost2 = cost
            
            cost = 0


print(cost)