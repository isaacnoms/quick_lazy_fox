#!/usr/bin/env python3

word_source = 'common_words.txt' #options: words.txt, common_words.txt (10000 most common english words in order of frequency)
words_list = []
search_letter = 'z'
search_results = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


for l in alphabet:
	search_letter = l
	with open(word_source) as words_file:
		for word in words_file:
			word = word.strip()
			word = word.lower()
			words_list.append(word)
			for n in word:
				if n == search_letter:
					search_results.append(word)
					break
	search_results.sort()

	file = open('common_' + search_letter + '.txt', 'w') 
	for w in search_results:
		file.write(w + '\n\')

print('Complete')