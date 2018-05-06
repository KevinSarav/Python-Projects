def flatten_list(lst):
    flatList = []
    for count in range(0, len(lst)):
        if type(lst[count]) == type([]):
            for countList in range(0, len(lst[count])):
                flatList.append(lst[count][countList])
        else:
            flatList.append(lst[count])
    return flatList

lst = ['reptile', ['cat', 'dog', 'horse'], 3.14, [1, 3, 5, 7], 'final']
print(flatten_list(lst))