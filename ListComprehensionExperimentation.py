import random, math
"""
x = [i for i in range(10)]
#This will give the output:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(x)

y = [i*i for i in range(10)]
#This will give the output:
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(y)

z = [i**i for i in range(10)]
#This will give the output:
[1, 1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489]
print(z)
"""

"""
conditional = True
List = range(10)

#this for loop is equivalent to the following list comprehension
expList = []
for item in List:
    if conditional:
        expression = item * item
        expList.append(expression)

expListComp = [item * item for item in List if conditional]

print(expList)
print(expListComp)
print("")
"""

"""
#ordered pair example:
OPList = []
for a in range(3):
	for b in range(3):
		OPList.append((a,b))

OPListComp = [(a, b) for a in range(3) for b in range(3)]

print(OPList)
print(OPListComp)
print("")

#reverse ordering example:
OPList2 = []
for a in range(3):
	for b in range(3):
		OPList2.append((b,a))

OPListComp2 = [(a, b) for b in range(3) for a in range(3)]

print(OPList2)
print(OPListComp2)
print("")
"""

"""
#print num random ints
num = 10
qwerty = [random.randint(1, 11) for i in range(num)]
print(qwerty)
print("")
"""

"""
#print random tuples
num2 = 10
randtuples = [(random.randint(1, 11), random.randint(1, 11)) for j in range(num2)]
print(randtuples)
"""

simulations = int(1e7)
#1d
print("1d means the number line from -10 to 10.")
randDigits = [random.uniform(-10, 10) for j in range(simulations)]
distOfDigits = [abs(num) for num in randDigits]
avgDigitDist = sum(distOfDigits)/len(distOfDigits)
print("Mean distance from 0 in 1d: " + str(round(avgDigitDist, 6)))
print("The mean distance is " + str(round(((avgDigitDist/10) * 100), 6)) + "% of the maximum distance.")
print("")

#2d
print("2d means the cartesian grid from (-10, -10) to (10, 10).")
randtuples2 = [(random.uniform(-10, 10), random.uniform(-10, 10)) for j in range(simulations)]
distOfTuples = [(math.sqrt(((T[0]) ** 2) + ((T[1]) ** 2))) for T in randtuples2]
avgDist = sum(distOfTuples)/len(distOfTuples)
print("Mean distance from (0, 0) in 2d: " + str(round(avgDist, 6)))
print("The mean distance is " + str(round(((avgDist/(10*math.sqrt(2))) * 100), 6)) + "% of the maximum distance.")
print("")

#3d
print("3d means the cartesian space from (-10, -10, -10) to (10, 10, 10).")
randTriple = [(random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(-10, 10)) for i in range(simulations)]
distOfTriple = [(math.sqrt(((T[0]) ** 2) + ((T[1]) ** 2) + ((T[2]) ** 2))) for T in randTriple]
avgDist2 = sum(distOfTriple)/len(distOfTriple)
print("Mean distance from (0, 0, 0) in 3d: " + str(round(avgDist2, 6)))
print("The mean distance is " + str(round(((avgDist2/(10*math.sqrt(3))) * 100), 6)) + "% of the maximum distance.")
print("")