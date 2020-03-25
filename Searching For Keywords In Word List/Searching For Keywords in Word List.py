with open("words.txt", mode="r") as words:
    words = [line.replace("\n", "") for line in words.readlines()]

wordSpecific = open("words with specific.txt", "w")

specificString = input("What is the keyword you want to search for? ")

for line in words:
    if specificString in line:
        wordSpecific.writelines(line + "\n")
        
wordSpecific.close()
with open("words.txt", mode="r") as words:
    words = [line.replace("\n", "") for line in words.readlines()]
​
wordSpecific = open("words with specific.txt", "w")
​
specificString = input("What is the keyword you want to search for? ")
​
for line in words:
    if specificString in line:
        wordSpecific.writelines(line + "\n")
        
wordSpecific.close()
