def vowel_checker(word):
	vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

	word = list(word)

	for element in word:
		if element in vowels:
			print(element)
			
vowel_checker('hello')