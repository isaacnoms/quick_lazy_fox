#!/usr/bin/env python3

alphabet = list(map(chr, range(ord('a'), ord('z')+1))) # generate alphabet as list

phrase = input('Enter phrase to check: ').lower()

for n in phrase:
	if n in alphabet:
		alphabet.remove(n)

if len(alphabet) > 0:
	print('The unused letters were: ' + ', '.join(alphabet))
else:
	print('All letters were used.')
