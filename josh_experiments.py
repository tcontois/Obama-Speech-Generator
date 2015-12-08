from collections import defaultdict
from textblob import TextBlob


def getwords():
	file = open('datasets/short_fp.txt')
	text = file.read()
	t = TextBlob(text.decode('ascii', 'ignore'))
	wordlist = t.tags
	taglist = {}
	print wordlist

	for k,v in wordlist:

		if v in taglist:
			taglist[v].append(k)
		else:
			taglist[v] = [k]
	#print taglist['NN']


def writeseq():
	filew = open('datasets/sequence.txt','w')
	file = open('datasets/short_fp.txt')
	text = file.read()
	t = TextBlob(text.decode('ascii', 'ignore'))
	wordlist = t.tags
	taglist = {}
	for k,v in wordlist:
		filew.write(v+" ")


if __name__ == '__main__':
	writeseq()

