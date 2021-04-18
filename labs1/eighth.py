# Write a program that counts the number words in
# the file and returns how many times each word is
# repeated
import re
file = open("C:/Users/Michal/PycharmProjects/PythonForEngineering/labs1/test.txt", 'r')
data = file.read().lower()
wordList = re.sub(r"[\".!,;?-]", " ",  data).split()

setOfWords = set(wordList)
wordUsage = {}
for word in setOfWords:
    wordUsage[word] = wordList.count(word)

for w in sorted(wordUsage, key=wordUsage.get, reverse=True):
    print(w, wordUsage[w])
