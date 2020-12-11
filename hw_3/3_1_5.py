banknot = [10, 20, 50, 100, 200, 500, 1000]
schetchik = [0, 0, 0, 0, 0, 0, 0]
print("Enter amount")
amount = int(input())
for i, j in zip(banknot, schetchik):
    if amount >= i: 
        j = amount // i
        if j > 10:
            j = 10
        amount = amount - j * i
        print(i, " : " , j)