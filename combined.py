#!/usr/bin/env python3
import random

words_list = []
sentence = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

with open('words.txt') as words_file:
	for word in words_file:
		word = word.strip()
		words_list.append(word)

while alphabet:
	rand_word = random.choice(words_list)
	sentence.append(rand_word)
	for n in range(len(rand_word)):
		if rand_word[n] in alphabet:
			alphabet.remove(rand_word[n])
		else: 
			continue

print(' '.join(sentence))