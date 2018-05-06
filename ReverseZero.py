totalInputList = []
inp = int(input())

while inp != 0:
    totalInputList.append(inp)
    inp = int(input())

totalInputList.append(inp)
while len(totalInputList) > 0:
    print(totalInputList.pop(), end = " ")
