import random
import sys

class Markov(object):

	def __init__(self, topic_file=None, topic_weight=1, chain_size=3):
		self.chain_size = chain_size
		self.cache = {}
		# self.open_file = open('./datasets/obama_speeches.txt')
		self.open_file = open('./datasets/hello.txt')
		self.topic_file = topic_file
		self.topic_weight = topic_weight
		self.words = self.file_to_words()
		self.word_size = len(self.words)
		self.database()

	def file_to_words(self):
		self.open_file.seek(0)
		data = self.open_file.read()
		words = data.split()
		if self.topic_file:
			self.topic_file.seek(0)
			topic_data = self.topic_file.read()
			self.topic_words = topic_data.split()
			self.topic_word_size = len(self.topic_words)
			for i in range(self.topic_weight):
				words = words + self.topic_words
		return words

	def words_at_position(self, i):
		"""Uses the chain size to find a list of the words at an index."""
		chain = []
		for chain_index in range(0, self.chain_size):
			chain.append(self.words[i + chain_index])
		return chain

	def topic_words_at_position(self, i):
		"""Uses the chain size to find a list of the words at an index."""
		chain = []
		for chain_index in range(0, self.chain_size):
			chain.append(self.topic_words[i + chain_index])
		return chain

	def chains(self):
		"""Generates chains from the given data string based on passed chain size.

		So if our string were:

			"What a lovely day"

		With a chain size of 3, we'd generate:

			(What, a, lovely)

		and

			(a, lovely, day)
		"""

		if len(self.words) < self.chain_size:
			return

		for i in range(len(self.words) - self.chain_size - 1):
			yield tuple(self.words_at_position(i))

	def database(self):
		for chain_set in self.chains():
			key = chain_set[:self.chain_size - 1]
			next_word = chain_set[-1]
			if key in self.cache:
				self.cache[key].append(next_word)
			else:
				self.cache[key] = [next_word]

	def generate_markov_text(self, size=25):
		# speech = 'Good afternoon. Please be seated. '
		speech = ''
		if self.topic_file:
			speech += self.generate_with_topic(size=size)
		else:
			speech += self.generate_without_topic(size=size)
		# speech += ' Thank you.'
		return speech

	def generate_without_topic(self, size=25):
		seed = random.randint(0, self.word_size - self.chain_size)
		while(self.words[seed-1][len(self.words[seed-1])-1] != '.' or self.words[seed][0].isupper() is False):
			seed = random.randint(0, self.word_size-self.chain_size)
		gen_words = []
		seed_words = self.words_at_position(seed)[:-1]
		gen_words.extend(seed_words)
		count = 0
		while(True):
			last_word_len = self.chain_size - 1
			last_words = gen_words[-1 * last_word_len:]
			next_word = random.choice(self.cache[tuple(last_words)])
			gen_words.append(next_word)
			count = count + 1
			if(count >= size and next_word[len(next_word)-1] in set(['.', '!', '?'])):
				break
		return ' '.join(gen_words)

	def generate_with_topic(self, size=25):
		seed = random.randint(0, self.topic_word_size - self.chain_size)
		while(self.topic_words[seed-1][len(self.topic_words[seed-1])-1] != '.' or self.topic_words[seed][0].isupper() is False):
			seed = random.randint(0, self.topic_word_size-self.chain_size)
		gen_words = []
		seed_words = self.topic_words_at_position(seed)[:-1]
		gen_words.extend(seed_words)
		count = 0
		while(True):
			last_word_len = self.chain_size - 1
			last_words = gen_words[-1 * last_word_len:]
			next_word = random.choice(self.cache[tuple(last_words)])
			gen_words.append(next_word)
			count = count + 1
			if(count >= size and next_word[len(next_word)-1] in set(['.', '!', '?'])):
				break
		return ' '.join(gen_words)

