from collections import defaultdict
gregorsDice = 8
gregorsSides = 5
oberynsDice = 4
oberynsSides =10
gregorsFace=[1,2,3,4,5]
oberynsFace=[1,2,3,4,5,6,7,8,9,10]
gregorsDict= defaultdict(float)
oberynsDict=defaultdict(float)
#This method is used as a way to calculate the number of ways a value can appear
def waysToMakeFace(throws, numFaces, amount):
    table = [[0]*(amount+1) for i in range(throws+1)]
    for j in range(1, min(numFaces+1,amount+1)):
        table[1][j]=1
    for i in range(2, throws + 1):
        for j in range(1, amount + 1):
            for k in range(1, min(numFaces + 1, j)):
                table[i][j] += table[i - 1][j - k]
    return table[-1][-1]

#Here we populate gregorsDict which is a hashtable where keys are the face value and the values are the probability of getting that face
for i in range(8,41):
    ways = waysToMakeFace(gregorsDice,gregorsSides,i)
    gregorsDict[i] += ways/pow(gregorsSides,gregorsDice)
print(gregorsDict)
#similar to the above for loop here it is done for obern's dice
for i in range(4,41):
    ways = waysToMakeFace(oberynsDice,oberynsSides,i)
    oberynsDict[i]+= ways/pow(oberynsSides,oberynsDice)
#Fininally we use the two dictionaries created to calculate the propability of gregor
sum=0
for i in range(8,41):
    gregorsProb = gregorsDict[i]
    oberynsProb =0
    for j in range(i+1):
        oberynsProb+=oberynsDict[j]
    sum+=gregorsProb*oberynsProb
#print the probibility that gregor will win
print(sum)
