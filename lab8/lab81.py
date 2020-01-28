def the_last_one(N, K):
    l = list(range(1, N+1))
    i = 1
    print(l)
    while len(l) > 1:
        if i % K == 0:
            print('Deleting ', l[0])
            l.pop(0)
            i = 1
        l.append(l.pop(0))
        i += 1
    else:
        print('The last one: ', l)


try:
    n = int(input('Enter the number of people: '))
    k = int(input('Enter step: '))
    the_last_one(n, k)
except ValueError:
    exit('Enter integer numbers please!!!')
