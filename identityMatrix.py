def generate_identity_matrix(n):
    identityMatrix = []
    for emptyLists in range(0, n):
        identityMatrix.append([])
    for column in range(0, n):
        for row in range(0, n):
            if column == row:
                identityMatrix[column].append(1)
            else:
                identityMatrix[column].append(0)
    return identityMatrix

n = 3
print(generate_identity_matrix(n))
n = 5
print(generate_identity_matrix(n))