def factorial_n(x):
    factorial = 1
    if x == 0:
        return 1
    else:
        for y in range(1, x + 1):
            factorial = factorial * y

        return factorial

for z in range(0, 6):
    x = int(input())
    print(factorial_n(x))