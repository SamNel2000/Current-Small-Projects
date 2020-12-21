Disarium = [] 														#Final Disarium Number List
upper = int(1e5)											        #Upper Bound
for n in range(0, upper + 1):									    #Loops through all number 0 to upper
	numposList = []													#Initialize temp list to save digits and position
	DisNum = 0														#Initialize Disarium calculation value
	for l in range(len(str(n))):									#Loop through the digits of n
		numposList.append(int(str(n)[l]))							#Add each digit to temp list
	for i in range(len(numposList)):								#Loop through temp list
		DisNum += numposList[i] ** (i+1)							#Power each digit according to position and add to total Disarium calculation
	if(DisNum == n):												#Check if Disarium calculation equals n
		Disarium.append(n)											#Add correct Disarium values to the list

print("These are the Disarium numbers between 0 and " + str(n))
print(Disarium)

