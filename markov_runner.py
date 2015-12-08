from __future__ import division
import markov_text_gen
import modified_markov
import tims_text_gen
from collections import defaultdict


if __name__ == '__main__':
	print "Welcome to Tim Text Gen"
	print "Please Choose a Topic: Foreign Policy (1) or Health Care (2)"
	topicno = input()
	if topicno is 1:
		topic = open('./datasets/short_fp.txt')
	if topicno is 2:
		topic = open('./datasets/short_health_care.txt')
	print "Please choose a GODDAMN CHAIN LENGTH MAN"
	chainlength = input()
	markov=modified_markov.Markov(topic_file=topic, topic_weight=50, chain_size=chainlength)
	print "Markov chain looking at previous 3 words:"
	print markov.generate_markov_text(size=50)
	# for i in range(2,5):
	# 	markov_modified=modified_markov.Markov(file_, chain_size=(i))
	# 	print markov_modified.generate_markov_text()
	# tims_markov=tims_text_gen.Markov(file_)
	# print "Markov chain looking at previous 2 words:"
	# print ''
	# print tims_markov.generate_markov_text()