import matplotlib.pyplot as plt
import pandas
nonAlphanumeric = ['}','{','[','^','-','.','/',']']
#opening textFile.txt
f = open("textFile", "r",encoding="utf-8")
print("running")

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

#sorting the final dictionary
final = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
x_axis = []
y_axis = []

for a in final.keys():
    if len(x_axis) == 10:
        break
    x_axis.append(a)
    y_axis.append(final[a])

plt.bar(range(len(y_axis)), y_axis, align='center')
plt.xticks(range(len(x_axis)), x_axis, size='small')
df = pandas.DataFrame(final.items(), columns=['Word', 'Count'])
df.to_csv('dictionary.csv')
plt.show()

