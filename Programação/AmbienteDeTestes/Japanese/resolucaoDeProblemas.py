from random import choice

def readlines():
	arq = open("japaneseWords.txt", "r")
	read = arq.readlines()
	words = choice(read)
	print(words)
	
readlines()