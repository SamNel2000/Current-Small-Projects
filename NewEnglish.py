import random

#starting strings2

#possible lengths of words
lengths = [2,3,4,5,6,7,8,9,10,11,12,13]
#relative frequencies of lengths
lengthWeight = [22,46,69,88,97,100,88,51,23,10,5,2]
vowels = "aeiou"
#relative frequencies of vowels
vowelWeights = (4,5,3,4,2)
consonants = "bcdfghjklmnpqrstvwxyz"
#relative frequencies of consonants
consonantWeights = (12,23,15,11,10,11,2,5,18,21,20,18,1,20,25,22,7,13,1,9,1)
all = vowels + consonants

"""
#chooses 1 letter
rand_char = random.choice(vowels)
#chooses sample of letters from given string
rand_samp = random.sample(all, 5)
#concats all letters from rand_samp
rand_samp_str = ''.join(rand_samp)
#selecting vowels using weights
Z = random.choices(vowels, weights = vowelWeights, k = 20)
print(''.join(Z))
#selecting consonants using weights
ZZ = random.choices(consonants, weights = consonantWeights, k = 20)
print(''.join(ZZ))
"""

#sentenceLen is the number of words
sentenceLen = 5
for n in range(sentenceLen):
	word = ""
	#randomly selects word length
	wordLength = (random.choices(lengths, weights = lengthWeight, k = 1))[0]
	creation = True
	addVow = 33
	while(creation):
		if(random.randint(1,100) > addVow):
			#add consonant
			word += ''.join(random.choices(consonants, weights = consonantWeights, k = 1))
			addVow += (100 - addVow) // 2
		else:
			#add vowel
			word += ''.join(random.choices(vowels, weights = vowelWeights, k = 1))
			addVow = addVow // 6
		if(len(word) == wordLength):
			break
	print(word, end = " ")
