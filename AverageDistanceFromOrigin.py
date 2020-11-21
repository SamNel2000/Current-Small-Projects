import random, math
simulations = int(1e5)
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