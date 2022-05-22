def comparison_checker(word_a,word_b):
	word_a = list(word_a)
	word_b = list(word_b)

	for element in word_a:
		if element in word_b:
			print(element)
			
comparison_checker('hello','undertaker')