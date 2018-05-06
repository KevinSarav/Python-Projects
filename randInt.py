def averageRand(x):
    import random

    randList = []
    for count in range(x, 0, -1):
        randList.append(random.randint(0, 100))
    average = 0
    for addUp in range(len(randList) - 1, -1, -1):
        average += randList[addUp]
        print(randList.pop(), end = " ")
    average /= x
    print("\n" + str(average))
    return average

for fourTimes in range(0, 4):
    x = int(input())
    averageRand(x)