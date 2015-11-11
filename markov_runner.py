from __future__ import division
import markov_text_gen
import modified_markov
from collections import defaultdict

file_=open('obama_speeches.txt')
markov=markov_text_gen.Markov(file_)
print "Markov chain looking at previous 2 words:"
print markov.generate_markov_text()
print "\nNow looking at previous 3 words \n"
markov_modified=modified_markov.Markov(file_, chain_size=3)
print markov_modified.generate_markov_text()