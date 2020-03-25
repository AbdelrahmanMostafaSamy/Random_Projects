import random

with open("numberfile.txt", mode="w+") as testfile:
    times_to_repeat = 101

    while times_to_repeat > 1:
        testfile.write("\n" + str(random.randint(1,100)))
        times_to_repeat -= 1
    
    testfile.seek(0)
    testfile = [line.replace('\n', '') for line in testfile.readlines()]

amountOfEvenNumbers = 0
amountOfOddNumbers = 0
for line in testfile:
	if line == "":
		continue
	if int(line)%2 == 0:
		amountOfEvenNumbers += 1
		print(f"{line} is an Even Number")
	elif int(line)%2 != 0:
		amountOfOddNumbers += 1
		print(f"{line} is an Odd Number")
        
print(f"\n\nAmount of Even Numbers are {amountOfEvenNumbers}, Amount of Odd Numbers are {amountOfOddNumbers}")
