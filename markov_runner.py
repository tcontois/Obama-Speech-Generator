from __future__ import division
import markov_text_gen
import modified_markov
import tims_text_gen
import random, string
from collections import defaultdict
from textblob import TextBlob
import nltk


''' 
This program contains two different ways to bias an generated speech. 
(1) The first way is to have the NGram model read a topic text many times to 
	make the likelihood it selects a word from their higher. The number of 
	times it reads the topic text is the topic_weight variable. 

(2) The second way we bias a generated text is to first 
'''


def topic_weight_bias():
	# topic = open('./datasets/short_health_care.txt')
	# topic = open('./datasets/short_fp.txt')
	topic = None
	markov=modified_markov.Markov(topic_file=topic, topic_weight=20, chain_size=3)
	print markov.generate_markov_text(size=50)


def noun_phrase_replacement():
	# topic = open('./datasets/short_health_care.txt')
	topic = open('./datasets/short_fp.txt')
	topic_text=topic.read()
	biased_noun_phrases=TextBlob(topic_text.decode('ascii','ignore')).noun_phrases

	markov=modified_markov.Markov(topic_file=None, topic_weight=20, chain_size=3)
	unbiased_text = markov.generate_markov_text(size=50)
	exclude = set(".,'!?")	
	unbiased_text = ''.join(ch for ch in unbiased_text if ch not in exclude)
	unbiased_text=unbiased_text.lower()
	t = TextBlob(unbiased_text.decode('ascii', 'ignore'))
	unbiased_noun_phrases=t.noun_phrases
	for np in unbiased_noun_phrases:
		if np not in biased_noun_phrases:
			try:
				np=np.encode('utf-8')
				index=unbiased_text.index(np)
				np_len=len(np)
				first_part=unbiased_text[:index]
				second_part=unbiased_text[(index+np_len):]
				if unbiased_text[index+np_len-1] is 's':
					new_np=random.choice(biased_noun_phrases)
					new_np=new_np.encode('utf-8')
					while  new_np[-1] != 's':
						new_np=random.choice(biased_noun_phrases)
						new_np=new_np.encode('utf-8')
				else:
					new_np=random.choice(biased_noun_phrases)
					new_np=new_np.encode('utf-8')
				new_np=new_np.upper()
				unbiased_text=first_part+new_np+second_part
			except:
				pass
	print unbiased_text




if __name__ == '__main__':
	topic_weight_bias()
	noun_phrase_replacement()

