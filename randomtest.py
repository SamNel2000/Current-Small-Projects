import random

trial = 1e7
count = 0
a_count = 0
b_count = 0
tie_count = 0

while(count < trial/2):
	a = random.randint(1,100)
	b = random.randint(1,100)
	if(a > b):
		a_count += 1
	elif(b > a):
		b_count += 1
	else:
		tie_count += 1
	count += 1
print("halfway done")
while(count < trial):
	a = random.randint(1,100)
	b = random.randint(1,100)
	if(a > b):
		a_count += 1
	elif(b > a):
		b_count += 1
	else:
		tie_count += 1
	count += 1

print("A: " + str(a_count) + " B: " + str(b_count) + " Ties: " + str(tie_count))