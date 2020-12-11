banknot = [1000, 500, 200, 100, 50, 20, 10]
schetchik = [0, 0, 0, 0, 0, 0, 0]
print('Skolko grivni nado?')
summa = int(input())
for i, j in zip(banknot, schetchik):
    if summa >=i:
        j = summa //i
        summa = summa - j * i
        print(i, " : ", j)