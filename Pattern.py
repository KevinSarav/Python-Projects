def print_pattern(n, m):
    for endColumn in range(n, 0, -1):
        for endRow in range(m, 0, -1):
            print("*", end = " ")
        print("\n")

n, m = int(input()), int(input())
print_pattern(n, m)