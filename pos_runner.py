from __future__ import division
import sequence
from collections import defaultdict

if __name__ == '__main__':
	open_file=open('./datasets/sequence.txt')
	pos_dictionary=open('./datasets/')

	sequence_markov=sequence.Markov(open_file)
	pos_sequence= sequence_markov.generate_markov_text()

	for tags in pos_sequence:
