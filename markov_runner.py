from __future__ import division
import markov_text_gen
import modified_markov
import tims_text_gen
import random, string
from collections import defaultdict
from textblob import TextBlob
import nltk




if __name__ == '__main__':
	# print "Welcome to Tim Text Gen"
	# print "Please Choose a Topic: Foreign Policy (1) or Health Care (2)"
	# topicno = input()
	# if topicno is 1:
	# 	topic = open('./datasets/short_fp.txt')
	# if topicno is 2:
	# 	topic = open('./datasets/short_health_care.txt')
	# print "Please choose a GODDAMN CHAIN LENGTH MAN"
	# chainlength = input()
	# print "How much do you weigh? (1-10)"
	# weight=input()
	# weight=weight*7
	# markov=modified_markov.Markov(topic_file=topic, topic_weight=weight, chain_size=chainlength)
	topic = open('./datasets/short_health_care.txt')

	# topic = open('./datasets/short_fp.txt')
	chainlength=3
	markov=modified_markov.Markov(topic_file=topic, topic_weight=50, chain_size=chainlength)
	print "Markov chain looking at previous %s words:" % chainlength
	print markov.generate_markov_text(size=50)

	# UNCOMMENT THE ABOVE LINE TO GENERATE THE CLASSIC MARKOV GENERATED TEXT

	
	# unbiased_text = markov.generate_markov_text(size=50)

	# markov=modified_markov.Markov(topic_file=None, topic_weight=0)
	# print "Actual Obama speech:"
	# print markov.get_actual_obama_speech(size=50)


	# unbiased_text = markov.generate_markov_text(size=50)

	# topic_text=topic.read()
	# biased_noun_phrases=TextBlob(topic_text.decode('ascii','ignore')).noun_phrases

	# # t = TextBlob(unbiased_text.decode('ascii', 'ignore'))
	# # unbiased_noun_phrases=t.noun_phrases
	# # print unbiased_noun_phrases

	# # print unbiased_text

	# exclude = set(".,'!?")	

	# unbiased_text = ''.join(ch for ch in unbiased_text if ch not in exclude)

	# unbiased_text=unbiased_text.lower()
	
	# t = TextBlob(unbiased_text.decode('ascii', 'ignore'))
	# unbiased_noun_phrases=t.noun_phrases

	# print unbiased_noun_phrases

	# for np in unbiased_noun_phrases:
	# 	if np not in biased_noun_phrases:
	# 		try:
	# 			np=np.encode('utf-8')
	# 			index=unbiased_text.index(np)
	# 			np_len=len(np)
	# 			first_part=unbiased_text[:index]
	# 			second_part=unbiased_text[(index+np_len):]
	# 			if unbiased_text[index+np_len-1] is 's':
	# 				print "TRUE ", np
	# 				new_np=random.choice(biased_noun_phrases)
	# 				new_np=new_np.encode('utf-8')
	# 				while  new_np[-1] != 's':
	# 					new_np=random.choice(biased_noun_phrases)
	# 					new_np=new_np.encode('utf-8')
	# 			else:
	# 				new_np=random.choice(biased_noun_phrases)
	# 				new_np=new_np.encode('utf-8')
	# 			new_np=new_np.upper()
	# 			unbiased_text=first_part+new_np+second_part
	# 		except:
	# 			pass

# 	unbiased_text=unbiased_text.lower()

# 	t = TextBlob(unbiased_text.decode('ascii', 'ignore'))
# 	unbiased_noun_phrases=t.noun_phrases

# 	# print unbiased_noun_phrases
# '''
# THE BELOW CODE SEARCHES THROUGH A MARKOV GENERATED TEXT SEQUENCE, IDENTIFIES THE NOUN PHRASES AND REPLACES 
# THEM WITH NOUN PHRASES FOUND IN OUR SUPER CONCENTRATED TOPIC FILES

# POSSIBLE THINGS TO CREATE: MAKE CHECKS TO MAKE THE SUBSTITUTIONS MORE SEEMLESS

# '''
# 	for np in unbiased_noun_phrases:
# 		if np not in biased_noun_phrases:
# 			try:
# 				np=np.encode('utf-8')
# 				index=unbiased_text.index(np)
# 				np_len=len(np)
# 				first_part=unbiased_text[:index]
# 				second_part=unbiased_text[(index+np_len):]
# 				if unbiased_text[index+np_len-1] is 's':
# 					print "TRUE ", np
# 					new_np=random.choice(biased_noun_phrases)
# 					new_np=new_np.encode('utf-8')
# 					while  new_np[-1] != 's':
# 						new_np=random.choice(biased_noun_phrases)
# 						new_np=new_np.encode('utf-8')
# 				else:
# 					new_np=random.choice(biased_noun_phrases)
# 					new_np=new_np.encode('utf-8')
# 				new_np=new_np.upper()
# 				unbiased_text=first_part+new_np+second_part
# 			except:
# 				pass

	# print unbiased_noun_phrases
	# print len(unbiased_noun_phrases)
	# print len(np_index)

	# print unbiased_text
	# print unbiased_noun_phrases
	# print biased_noun_phrases





	# for i in range(2,5):
	# 	markov_modified=modified_markov.Markov(file_, chain_size=(i))
	# 	print markov_modified.generate_markov_text()
	# tims_markov=tims_text_gen.Markov(file_)
	# print "Markov chain looking at previous 2 words:"
	# print ''
	# print tims_markov.generate_markov_text()
