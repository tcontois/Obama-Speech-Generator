from collections import defaultdict
from textblob import TextBlob
import sequence
import random

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
	return taglist



def writeseq():
	filew = open('datasets/sequence.txt','w')
	file = open('datasets/obama_speeches.txt')
	text = file.read()
	t = TextBlob(text.decode('ascii','ignore'))
	#t = TextBlob("Hello. This is a sample text. I fuckin hate alex lSSALLE.! yes !")
	wordlist = t.tags
	taglist = {}
	for k,v in wordlist:
		filew.write(v+" ")


if __name__ == '__main__':
	writeseq()
	sequence_file=open('./datasets/sequence.txt')
	word_file=open('./datasets/obama_speeches.txt')
	pos_dictionary=getwords()
	sequence_markov=sequence.Markov(sequence_file)
	word_markov=sequence.Markov(word_file)
	word_markov_cache=word_markov.database()
	pos_sequence= sequence_markov.generate_markov_text().split()
	sentence=[]
	first=True
	for tags in pos_sequence:
		next_words_pos=pos_dictionary[tags]
		if (first):
			next_word=random.choice(next_words_pos)
			sentence.append(next_word)
			first=False
		else:
			next_works_markov=word_markov_cache[sentence[-1]]
			next_words_pos.intersect
			next_words=set(next_words_pos).intersection(next_works_markov)
			sentence.append(random.choice(next_word))
			break

	print ' '.join(sentence)
