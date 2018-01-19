#!/usr/bin/env python3
import random

words_list = []
cut_off = 50
phrase = 'the quick brown fox jumps over the lazy dog' #len == 43

with open('words.txt') as words_file:
	for word in words_file:
		word = word.strip()
		word = word.lower()
		words_list.append(word)


def create():
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	sentence = []
	while alphabet:
		if len(' '.join(sentence)) > cut_off:
			break
		rand_word = random.choice(words_list)
		sentence.append(rand_word)
		for n in range(len(rand_word)):
			if rand_word[n] in alphabet:
				alphabet.remove(rand_word[n])
			else: 
				continue
	sentence = ' '.join(sentence)
	return(sentence)


sentence = create()

while len(sentence) > cut_off:
	sentence = create()

print(len(sentence))
print(sentence)