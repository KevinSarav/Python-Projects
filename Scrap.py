files = open('file_names.txt')
fileNames = files.readlines()
dictList = []
matrix = []
total_files = len(fileNames)

def print_matrix(m, l):
    print("%-*s" % (40, " "), end = "")
    for i in l:
        print(i[:-1], end = "\t")
    print()
    for i in range(len(m[0])):
        print("%-*s" % (40, l[i][:-1]), end = "")
        for j in range(len(m[0])):
            print("%*.2f" % (15, m[i][j]), end = " ")
        print()

def count_words(contents):
    dict = {}
    for line in contents:
        wordList = line.split()
        for word in wordList:
            if word not in dict:
                dict[word] = 1
            else:
                dict[word] += 1
    return dict

def count_word_overlap(i, j):
    overall = 0
    percentage = 0
    overall = max(sum(i.values()), sum(j.values()))
    for word1 in i:
        if word1 in j:
            percentage += min(i[word1], j[word1])
    percentage /= overall
    percentage *= 100
    return percentage

for line in fileNames:
    file = open(line[:-1], encoding = "utf8")
    print("Processing file: %s" %line)
    content = file.read()
    dictList.append(count_words(content))
    file.close()

for i in range(total_files):
    matrix.append([0] * total_files)
    for j in range(total_files):
        matrix[i][j] = count_word_overlap(dictList[i], dictList[j])

print_matrix(matrix, fileNames)
