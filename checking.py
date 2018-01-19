#!/usr/bin/env python3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

phrase = input('Enter phrase to check: ').lower()

for n in phrase:
	if n in alphabet:
		alphabet.remove(n)

if len(alphabet) > 0:
	print('The unused letters were: ' + ', '.join(alphabet))
else:
	print('All letters were used.')
