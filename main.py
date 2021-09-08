import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5],[1,1/2,1/3,1/4,1/5])
nonAlphanumeric = ['[','^','-','.','/',']']
f = open("textFile", "r")


stringText = str(f.read()).upper()
for a in nonAlphanumeric:
    stringText.replace('a','')
wordList = list(map(str,stringText.split(' ')))

dictionary = {}
def appendWord(word):
    global dictionary
    if word not in dictionary.keys():
        dictionary[word] = 1
    else:
        dictionary[word]+=1

for currentWord in wordList:
    if currentWord.isnumeric() == False:
        appendWord(currentWord)

y_axis = []
x_axis = [x for x in range(1,len(dictionary.keys())+1)]

final = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
print(final)
plt.ylabel('some numbers')
plt.show()

