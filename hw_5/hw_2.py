
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
num4 = int(input("Enter 4th number: "))
num5 = int(input("Enter 5th number: "))
numbers = [num1, num2, num3, num4, num5]


def sq(x):
    if x >= 2:
        for y in range(2, x):
            if not (x % y):
                return str(x) + " --> This is not a prime number"
    else:
        return "This is not a prime number"
    return str(x) + " --> " + str(x ** 2)


squared_numbers = list(map(sq, numbers))
print(squared_numbers)
