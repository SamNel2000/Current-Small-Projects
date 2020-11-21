import random

a = list(range(1,11))
for num in range(len(a)):
	for val in a:
		print(str(num) + ":", str(val) + " ", end = '')

print(" ")
for val in a:
	for num in range(len(a)):
		print(str(num) + ":", str(val) + " ", end = '')