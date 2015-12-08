from collections import defaultdict
from textblob import TextBlob
#coding: utf-8

def getwords():
	filew = open('datasets/dictionaryforalex.txt','w')
	file = open('datasets/short_fp.txt')
	text = file.read()
	t = TextBlob(text.decode('ascii', 'ignore'))
	#t = TextBlob(text)
	wordlist = t.tags
	taglist = {}
	#print wordlist
	for k,v in wordlist:
		filew.write(k+" "+v+'\n')
		if v in taglist:
			taglist[v].append(k)
		else:
			taglist[v] = [k]
	#filew.write(taglist)
	#print taglist['NN']


def writeseq():
	filew = open('datasets/sequence.txt','w')
	file = open('datasets/foreign_policy.txt')
	text = file.read()
	t = TextBlob(text.decode('ascii','ignore'))
	#t = TextBlob("Hello. This is a sample text. I fuckin hate alex lSSALLE.! yes !")
	wordlist = t.tags
	print wordlist
	taglist = {}
	for k,v in wordlist:
		filew.write(v+" ")


if __name__ == '__main__':
	getwords()

