#!/usr/bin/env python3

cut_off = 80
word_source = 'common_words.txt' #options: words.txt, common_words.txt (10000 most common english words in order of frequency)
words_list = []
sentences_list = []
sentence = []
counter = 0
output_file = 'sentences.txt'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
phrase = 'the quick brown fox jumps over the lazy dog' #len == 43

with open(word_source) as words_file:
	for word in words_file:
		word = word.strip()
		word = word.lower()
		words_list.append(word)
words_list.sort()

n_words = len(words_list)



for n in range(n_words):
	#resetting all the variablessss
	sentence = []
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	word = words_list[n]
	for l in word:
		if l in alphabet:
			alphabet.remove(l)
		else:
			continue

	sentence.append(word)
	print(sentence)
	#while alphabet:
