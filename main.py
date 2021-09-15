import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5],[1,1/2,1/3,1/4,1/5])
nonAlphanumeric = ['[','^','-','.','/',']']
#opening textFile.txt
f = open("textFile", "r",encoding="utf-8")


stringText = str(f.read()).upper()
#replacing/removing all non-alphanumeric characters
for a in nonAlphanumeric:
    stringText.replace(a,'')

wordList = list(map(str,stringText.split(' ')))

dictionary = {}
def appendWord(word):
    global dictionary
    if word not in dictionary.keys():
        dictionary[word] = 1
    else:
        dictionary[word]+=1

for currentWord in wordList:
    if currentWord.isnumeric() == False and currentWord not in nonAlphanumeric:
        appendWord(currentWord)

y_axis = []
x_axis = [x for x in range(1,len(dictionary.keys())+1)]

#sorting the final dictionary to be ordered and used in graph later
final = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
print(final)
plt.ylabel('some numbers')
plt.show()

