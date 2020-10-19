def break_words(stuff):
	"""this function will break up words for us. """
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words."""
	return sorted(words) 
	'''
		sorted() 函数对所有可迭代的对象进行排序操作。

		sort 与 sorted 区别：

		sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。

		list 的 sort 方法返回的是对已经存在的列表进行操作，
		而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
	'''

def print_first_word(words):
	"""prints the first word after popping it off"""
	word = words.pop(0)
	print(word)

def print_last_word(words):
	"""prints the last word after popping it off"""
	word = words.pop(-1)
	print(word)

def sort_sentence(sentence):
	"""take in a full sentence and returns the sorted words"""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""print the first and last words of the sentence"""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""sort the words then print the first and last one"""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
