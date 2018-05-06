def hailstone_numbers(x):
    while x != 1:
        if x % 2 == 1:
            x = x * 3 + 1
            print(int(x), end=", ")
        elif x != 2 and x % 2 == 0:
            x /= 2
            print(int(x), end=", ")
        else:
            x /= 2
            print(int(x))

x = int(input())
hailstone_numbers(x)