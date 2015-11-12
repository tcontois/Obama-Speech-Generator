from __future__ import division
import markov_text_gen
import modified_markov
import tims_text_gen
from collections import defaultdict

file_=open('obama_speeches.txt')
# markov=markov_text_gen.Markov(file_)
# print "Markov chain looking at previous 2 words:"
# print markov.generate_markov_text()
# markov=markov_text_gen.Markov(file_)
#print "Markov chain looking at previous 2 words:"
# print markov.generate_markov_text()
for i in range(2,5):
	markov_modified=modified_markov.Markov(file_, chain_size=(i))
	print "Examples with chain length %s" %i
	for j in range(10):
		print "Example #%s: \n" %(j+1) + markov_modified.generate_markov_text()
# tims_markov=tims_text_gen.Markov(file_)
# print "Markov chain looking at previous 2 words:"
# print ''
# print tims_markov.generate_markov_text()