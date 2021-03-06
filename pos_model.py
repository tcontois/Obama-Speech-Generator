from collections import defaultdict
from textblob import TextBlob
import nltk
import sequence
import random
import modified_markov

'''
This program was an early attempt at creating a text generation model.
We use an NLTK tagger we found and tag the database of over 300 obama_speeches
made by President Obama. We create a large dictionary where each key
is a part of speech and the values associated with it are words that 
fit that tag. We then grab a sequence of POS tags which will be the basis of our
sentence. We iteratore over the tags selecting the words that match the part of speech.
Because this would be create nonsense sentences, we also use our markov program. 
We find the intersection of the words that match the given POS and the words
that have been seen follow the previous word. If this intersection is empty a
random word is selected. 
'''

def getwords():
	# filew = open('datasets/dictionaryforalex.txt','w')
	file = open('datasets/obama_speeches.txt')
	text = file.read()
	tokens = nltk.word_tokenize(text.decode('ascii', 'ignore'))
	tagged = nltk.pos_tag(tokens)
	taglist = {}
	for k,v in tagged:
		# filew.write(k+" "+v+'\n')
		if v in taglist:
			taglist[v].append(k)
		else:
			taglist[v] = [k]
	return taglist



def writeseq():
	filew = open('datasets/sequence.txt','w')
	file = open('datasets/obama_speeches.txt')
	text = file.read()
	tokens = nltk.word_tokenize(text.decode('ascii','ignore'))
	tagged = nltk.pos_tag(tokens)
	for k,v in tagged:
		filew.write(v+" ")


if __name__ == '__main__':
	# writeseq()
	pos_dictionary=getwords()
	punctuation = set([".", "!", "?", ",", ";"])

	# word_markov=modified_markov.Markov()
	# topic = open('./datasets/short_fp.txt')
	topic = open('./datasets/short_health_care.txt')
	word_markov=modified_markov.Markov(topic_file=topic, topic_weight=50, chain_size=3)


	sequence_file=open('./datasets/sequence.txt')
	sequence_markov=sequence.Markov(sequence_file)
	
	pos_sequence = sequence_markov.get_tag_sequence().split()
	sentence=[]
	first = True
	for tag in pos_sequence:
		if first:
			first = False
			next_word=random.choice(pos_dictionary[tag])
			tries = 0
			while(next_word[0].isupper() is False and tries < 1000):
				tries += 1
				next_word=random.choice(pos_dictionary[tag])
			sentence.append(next_word)
		else:
			if tag in punctuation:
				sentence[-1] += tag
			else:
				tag_options = pos_dictionary[tag]
				cache_options = word_markov.get_cache_list(words_seq=sentence)
				if(cache_options is not None):
					intersection = [w for w in cache_options if unicode(w, "utf-8") in tag_options]
					if(len(intersection) < 1):
						next_word=random.choice(pos_dictionary[tag])
					else:
						next_word=random.choice(intersection)
				else:
					next_word=random.choice(pos_dictionary[tag])

				sentence.append(next_word)

	print ' '.join(sentence)
