import random

class Markov(object):

	def __init__(self, open_file, chain_size=2):
		self.chain_size = chain_size
		self.cache = {}
		self.open_file = open_file
		self.words = self.file_to_words()
		self.word_size = len(self.words)
		self.database()

	def file_to_words(self):
		self.open_file.seek(0)
		data = self.open_file.read()
		words = data.split()
		return words

	def words_at_position(self, i):
		"""Uses the chain size to find a list of the words at an index."""
		chain = []
		for chain_index in range(0, self.chain_size):
			chain.append(self.words[i + chain_index])
		return chain

	def chains(self):
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
		return self.cache

	def generate_markov_text(self, size=35):
		seed = random.randint(0, self.word_size - 3)
		gen_words = []
		seed_words = self.words_at_position(seed)[:-1]
		gen_words.extend(seed_words)
		for i in xrange(size):
			last_word_len = self.chain_size - 1
			last_words = gen_words[-1 * last_word_len:]
			next_word = random.choice(self.cache[tuple(last_words)])
			gen_words.append(next_word)
		return ' '.join(gen_words)

	def get_tag_sequence(self, size=35):
		seed = random.randint(0, self.word_size - size)
		punctuation = set([".", "!", "?"])
		count = 0;
		tags = []
		while(seed != 0 and self.words[seed-1] not in punctuation and count < 1000):
			count += 1
			seed = random.randint(0, self.word_size - size)
		tags.append(self.words[seed])
		num = 0
		while(num < size or self.words[seed] not in punctuation):
			seed += 1
			num += 1
			if(seed >= self.word_size - 1):
				break
			tags.append(self.words[seed])
		return ' '.join(tags)




