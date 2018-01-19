#!/usr/bin/env python3
import string

alphabet = list(string.ascii_lowercase)

phrase = input('Enter phrase to check: ').lower()

for n in phrase:
	if n in alphabet:
		alphabet.remove(n)

if len(alphabet) > 0:
	print('The unused letters were: ' + ', '.join(alphabet))
else:
	print('All letters were used.')
