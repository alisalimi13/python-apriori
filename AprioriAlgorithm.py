# In The Name Of Allah
# Program Name: Apriori
# Purpose: Finding frequent patterns from Retail data set using apriori algorithm
# programmer: Ali Salimi
# Date: 1396/8/25

# Defining And Initializing
dataSetLocation = 'retail.dat'
dataSet = []    # data set
itemSet = []    # item set
C = [[]]  # candidates
Cf = [[]]   # candidates frequency
F = [[]]  # frequents
minSup = 1800    # minimum support

# Preparing Data
print('Preparing Data: ')

# Reading Data From Local File
print('Reading Data Set From Local File...', end='\t')
for line in open(dataSetLocation):
    line = line.replace(" \n", '')
    dataSet.append(line.split(' '))
print('Done :)')

# Modifying Data Set And Creating Item Set
print('Modifying Data Set And Getting Item Set...', end='\t', flush=True)
i = 0
for a in dataSet:
    j = 0
    for b in a:
        dataSet[i][j] = int(dataSet[i][j])
        if dataSet[i][j] not in itemSet:
            itemSet.append(dataSet[i][j])
        j += 1
    i += 1
print('Done :)\n')

# Finding Frequent Patterns
print('Finding Frequent Patterns...')

# creating c1
C.append([])
Cf.append([])
for i in itemSet:
    C[1].append([i])
    Cf[1].append(0)

# finding f1 and c2
for i in dataSet:
    for j in i:
        Cf[1][j] += 1
F.append([])
a = 0
for i in Cf[-1]:
    if i >= minSup:
        F[-1].append(C[-1][a])
    a += 1
C.append([])
Cf.append([])
for i in range(0, len(F[-1])):
    for j in range(i+1, len(F[-1])):
        C[-1].append([F[-1][i][0], F[-1][j][0]])
        Cf[-1].append(0)

# finding other frequent patterns
while True:
    for i in dataSet:
        a = 0
        for x in C[-1]:
            for y in x:
                if y not in i:
                    break
            else:
                Cf[-1][a] += 1
            a += 1

    F.append([])
    a = 0
    for i in Cf[-1]:
        if i >= minSup:
            F[-1].append(C[-1][a])
        a += 1

    if len(F[-1]) == 0:
        break

    C.append([])
    Cf.append([])
    for i in range(0, len(F[-1])):
        for j in range(i+1, len(F[-1])):
            for k in range(2, len(F[-1][i])+1):
                if F[-1][i][-k] != F[-1][j][-k]:
                    break
            else:
                C[-1].append(F[-1][i] + [F[-1][j][-1]])
                Cf[-1].append(0)

    if len(C[-1]) == 0:
        break

print('Done :)\n')


# Print Frequent Patterns
print('Frequent Patterns:', F)
