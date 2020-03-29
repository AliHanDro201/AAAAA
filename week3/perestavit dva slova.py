a = input()
word1 = a[:a.find(' ')]
word2 = a[a.find(' ') + 1:]
print(word2 + ' ' + word1)
