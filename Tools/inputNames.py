import markdown
import codecs 

hello = "# "
title = input("Title: ")
fileName = input("Filename:")
fileName += ".html"

numberOfLists = int(input("Number of Lists: "))
#umberOfLists = int(numberOfLists)
lists = []
titles = []
print(fileName)

hello += title + "\n"
for k in range (0, numberOfLists):
	tempName = input("List Name: ")
	titles.append(tempName)
	tempList = []
	while True:
		temp = input("Name: ")
		if not temp:
			break
		tempList.append(temp)

	lists.append(tempList)

for j in range (0, numberOfLists):
	hello += "## " + titles[j] + "\n"
	currentList = lists[j]
	currentList.sort()
	for i in range(0, len(currentList)):
		hello += "* [ ]" + currentList[i] +  "\n"


html = markdown.markdown(hello, extensions=['markdown_checklist.extension'])

output_file = codecs.open(fileName, "w", 
                          encoding="utf-8", 
                          errors="xmlcharrefreplace"
)
output_file.write(html)

