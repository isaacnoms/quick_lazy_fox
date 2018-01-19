#!/usr/bin/env python3
import random

word_source = 'common_words.txt' #options: words.txt, common_words.txt (10000 most common english words in order of frequency)
words_list = []
letter_words_list = []
sentences_list = []
sentence = []

output_file = 'sentences.txt'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
phrase = 'the quick brown fox jumps over the lazy dog' #len == 43

smallest = open('smallest.txt', 'r')
smallest = smallest.read()
smallest = smallest.split(' ')

with open(word_source) as words_file:
	for word in words_file:
		word = word.strip()
		word = word.lower()
		words_list.append(word)
words_file.close()
words_list.sort()
n_words = len(words_list)

print(len(' '.join(smallest)))
print('main phase start')
for n in range(100):
	#resetting all the variablessss
	sentence = []
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	while alphabet and len(' '.join(sentence)) < len(' '.join(smallest)):
		letter = random.choice(alphabet)
		with open('common_' + letter + '.txt') as words_file:
			for word in words_file:
				word = word.strip()
				word = word.lower()
				letter_words_list.append(word)
		words_file.close()
		word = random.choice(letter_words_list)
		for l in word:
			if l in alphabet:
				alphabet.remove(l)
			else:
				continue
		sentence.append(word)
	if len(alphabet) == 0:
		sentences_list.append(sentence)

	if len(' '.join(sentence)) < len(' '.join(smallest)):
		print(len(' '.join(sentence)))
		print(sentence)
		smallest = sentence
smallest_file = open('smallest.txt', 'w')
smallest_file.write(' '.join(smallest))
print(smallest)
