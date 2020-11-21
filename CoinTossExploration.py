#written 11/21/20 to prove Bi's intuition wrong. :)

import random, secrets, statistics

#testing secrets module
#for x in range(1000):
	#print(secrets.randbelow(2))
#testing stats module
#M = statistics.mean([1,2,3,4,5])
#print(M)

simSizeList = [10, 100, 1000] #number of coin flips in a trial
trialNum = 1000 #number of trials

print("Each simulation has " + str(trialNum) + " trials.", end = "\n\n")
for s in simSizeList: #what size of simulation
	print("For " + str(s) + " coin flips:")
	CDList = []
	CDZ = 0
	for t in range(1, trialNum+1): #num of sims per trial
		#print("Sim #" + str(t) + " of size " + str(s) +":") #print Sim number
		heads = 0 #0 is head
		tails = 0 #1 is tail	
		for i in range(s): #i represents coin flip
			coin = random.randint(0,1)
			if coin == 0:
				heads += 1
			else:
				tails += 1
		countDiff = int(abs(heads - tails) / 2)
		CDList.append(countDiff)
		if countDiff == 0:
			CDZ += 1
		"""
		print(str(heads) + " were heads and " + str(tails) + " were tails.")
		print("The actual count was " + str(countDiff) + " off from expected.")
		print("The actual proportion was " + str(propDiff) + " off from expected.")
		"""
	mCD = statistics.mean(CDList)
	#print(CDList)
	print("The average deviation from " + str(int(s/2)) + " heads is: " + str(mCD) +
	 " or " + str(round(((mCD / s) * 100), 5)) + "% off 50/50.")
	print("There were equal heads to tails " + str(CDZ) + " times out of " + str(trialNum) + " ("+ str((CDZ/trialNum) * 100) + "%)")
	print("")