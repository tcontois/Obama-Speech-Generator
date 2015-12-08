from collections import defaultdict
from textblob import TextBlob


def analyze():
	file = open('datasets/short_fp.txt')
	text = file.read()
	t = TextBlob(text.decode('ascii', 'ignore'))
	wordlist = t.tags
	taglist = {}
	#print wordlist
	for k,v in wordlist:
		if v in taglist:
				taglist[v].append(k)
		else:
			taglist[v] = [k]
	print taglist['NN']



if __name__ == '__main__':
	analyze()

