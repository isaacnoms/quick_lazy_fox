#!/usr/bin/env python3
import random

words_list = []
sentence = []

with open('words.txt') as words_file:
	for word in words_file:
		word = word.strip()
		words_list.append(word)

for i in range(5):
	sentence.append(random.choice(words_list))

print(' '.join(sentence))


