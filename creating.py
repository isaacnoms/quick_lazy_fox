#!/usr/bin/env python3
import random

words_list = []
sentence = []

with open('common_words.txt') as words_file:
	for word in words_file:
		word = word.strip()
		words_list.append(word)

while input ('> ') == '':
	print(random.choice(words_list))
