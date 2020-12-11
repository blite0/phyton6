with open ('numbers.txt') as file:
    for line in file:
        a = line.split(' ')
        fizz = int(a[0])
        buzz = int(a[1])
        limit = int(a[2])
        for i in range(1, limit + 1):
            if i % fizz == 0 and i % buzz == 0:
                print('FB', end = ' ')
            elif i % fizz == 0:
                print('F', end = ' ')
            elif i % buzz == 0:
                print('B', end = ' ')
            else:
                p = print (i, end = ' ')
        print('\n Числа в строке из файла - ' + line)
