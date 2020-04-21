fileInput = open('input.txt', 'r', encoding='utf8')
scoreList = []
k = int(fileInput.readline())
for line in fileInput:
    i = line.split()
    if int(i[-1]) >= 40 and int(i[-2]) >= 40 and int(i[-3]) >= 40:
        scoreList.append(int(i[-1]) + int(i[-2]) + int(i[-3]))
fileInput.close()
lenScoreList = len(scoreList)
scoreList.sort()
 
 
def minScore(n, k, sL):
    if n <= k:
        return 0
    elif sL[-k] == sL[n + 1]:
        return 1
    for i in range(-k, -1):
        if sL[i] < sL[i + 1]:
            return sL[i + 1]
 
 
print(minScore(lenScoreList, k, scoreList))
