from __future__ import division
import markov_text_gen
import modified_markov
import tims_text_gen
from collections import defaultdict

# file_=open('obama_speeches.txt')
# markov=markov_text_gen.Markov(file_)
# print "Markov chain looking at previous 2 words:"
# print markov.generate_markov_text()
markov=modified_markov.Markov(chain_size=2)
print "Markov chain looking at previous 2 words:"
print markov.generate_markov_text()
# for i in range(2,5):
# 	markov_modified=modified_markov.Markov(file_, chain_size=(i))
# 	print markov_modified.generate_markov_text()
# tims_markov=tims_text_gen.Markov(file_)
# print "Markov chain looking at previous 2 words:"
# print ''
# print tims_markov.generate_markov_text()