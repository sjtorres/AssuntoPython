# - Tabuada do 1ao 10 com While

t = 1

while t <= 10:
    n = 1
    print('Tabuada do %d' %t)
    while n <= 10:
        print('%d X %d = %d' %(t, n, t*n))
        n += 1
    t += 1