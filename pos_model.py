from collections import defaultdict
from textblob import TextBlob
import nltk
import sequence
import random

def getwords():
	filew = open('datasets/dictionaryforalex.txt','w')
	file = open('datasets/obama_speeches.txt')
	text = file.read()
	# t = TextBlob(text.decode('ascii', 'ignore'))
	# wordlist = t.tags
	tokens = nltk.word_tokenize(text.decode('ascii', 'ignore'))
	tagged = nltk.pos_tag(tokens)
	taglist = {}
	#print wordlist
	for k,v in tagged:
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
	# t = TextBlob(text.decode('ascii','ignore'))
	tokens = nltk.word_tokenize(text.decode('ascii','ignore'))
	tagged = nltk.pos_tag(tokens)
	for k,v in tagged:
		filew.write(v+" ")


if __name__ == '__main__':
	# writeseq()
	sequence_file=open('./datasets/sequence.txt')
	word_file=open('./datasets/obama_speeches.txt')
	pos_dictionary=getwords()
	# sequence_markov=sequence.Markov(sequence_file)
	word_markov=sequence.Markov(word_file)
	word_markov_cache=word_markov.database()
	# pos_sequence= sequence_markov.generate_markov_text().split()
	pos_sequence= " PRP MD VB IN DT NN CC DT NN IN PRP VBP VBN UH PRP MD VB CC VB NNP IN DT JJ NN CC PRP MD VB PRP IN VBG DT NN IN NN NN RB IN VBG NNS TO VB NNS IN NNS RBR"
	pos_sequence=pos_sequence.split()
	sentence=[]
	first=True
	for tags in pos_sequence:
		intersection=[]
		if len(sentence)==0:
			next_word=random.choice(pos_dictionary[tags])
			sentence.append(next_word)
		else:
			next_word=sentence[-1]
			for words in word_markov_cache[(next_word,)]:
				uwords= unicode(words, "utf-8")
				if uwords in pos_dictionary[tags]:
					intersection.append(words)
			if len(intersection)>0:
				next_word=random.choice(intersection)
				print intersection
			else:
				print "Intersection Empty"
				next_word=random.choice(pos_dictionary[tags])
			sentence.append(next_word)
		print ' '.join(sentence)

	print ' '.join(sentence)
