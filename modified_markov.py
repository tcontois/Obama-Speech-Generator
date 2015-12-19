import random
import sys

class Markov(object):

	def __init__(self, topic_file=None, topic_weight=1, chain_size=3):
		self.chain_size = chain_size
		self.cache = {}
		self.open_file = open('./datasets/obama_speeches.txt')
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
		speech = ""
		# speech = self.generate_opening()
		# speech += " "
		if self.topic_file:
			speech += self.generate_with_topic(size=size)
		else:
			speech += self.generate_without_topic(size=size)
		speech += " "
		# speech += self.generate_ending()
		return speech

	def generate_opening(self):
		openings = ["Good afternoon.", "Hello, everybody!", "Hello.", "Thank you.", "Thank you, everybody.", "Please be seated.", 
			"All right, everybody go ahead and have a seat.", "How is everybody doing today?", "Thank you so much.",
			"If everybody has chairs, go ahead and use them.", "Look at all of you.", "Goodness.", "Thank you!",
			"Giving all praise and honor to God for bringing us here today.", "I am so grateful to see all of you.",
			"You guys are still cheering back there?", "Hello!", "I got a lot to say here.", "It is great to be here.",
			"It's good to be back with some real Patriots.", "I love you!", "It is great to be back.", "Hey!",
			"Please have a seat.", "Thank you very much.", "Good morning.", "Good morning, everybody."]
		text = []
		num_openings = random.randint(1,3)
		for i in range(num_openings):
			index = random.randint(0, len(openings)-1)
			text += openings[index].split() 
		return ' '.join(text)

	def generate_ending(self):
		endings = ["Thanks.", "Thank you!", "God bless you.", "God bless the United States of America.",
			"Thank you very much.", "Thank you very much, everybody.", "God bless America.", "Good bye.",
			"Have a good night."]
		text = []
		num_endings = random.randint(1,2)
		for i in range(num_endings):
			index = random.randint(0, len(endings)-1)
			text += endings[index].split()
		return ' '.join(text)

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

	def get_cache_list(self, words_seq=None):
		if(len(words_seq) < self.chain_size - 1):
			return None
		else:
			last_word_len = self.chain_size - 1
			# last_words = words_seq[-1 * last_word_len:]
			last_words = []
			for i in range(1, last_word_len+1):
				# last_words.append(str(words_seq[-1*i]))
				last_words.insert(0, str(words_seq[-1*i]))
			if(tuple(last_words) in self.cache):
				return self.cache[tuple(last_words)]
			else:
				return None

	def get_actual_obama_speech(self, size=25):
		seed = random.randint(0, self.word_size - size)
		while(self.words[seed-1][len(self.words[seed-1])-1] != '.' or self.words[seed][0].isupper() is False):
			seed = random.randint(0, self.word_size-self.chain_size)
		gen_words = []
		gen_words.append(self.words[seed])
		count = 0
		while(seed < self.word_size):
			count += 1
			seed += 1
			next_word = self.words[seed]
			gen_words.append(next_word)
			if(count >= size and next_word[len(next_word)-1] in set(['.', '!', '?'])):
				break
		return ' '.join(gen_words)

