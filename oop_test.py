import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
	"class %%%(%%%):":
	  "Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __int__(self, ***)":
	  "class %%% has-a __init__that takes slef and *** params.",
	"class %%%(object):\n\tdef ***(self, @@@)":
	  "class %%% has-a function *** that takes self and @@@ params.",
	"*** = %%%()":
	  "Set *** to an instance of class %%%",
	"***.***(@@@)":
	  "From *** get the *** function, call it with params self, @@@.",
	"***.*** = '***'":
	  "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english": 
	'''
	
	'''
	PHRASES_FIRST = True
else:
	PHRASES_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines(): #
'''
import urllib.request
url = "http://tieba.baidu.com"
response = urllib.request.urlopen(url)
html = response.read()         # 获取到页面的源代码
print(html.decode('utf-8'))    # 转化为 utf-8 编码

readlines() 方法用于读取所有行(直到结束符 EOF)并返回列表，
该列表可以由 Python 的 for... in ... 结构进行处理。
如果碰到结束符 EOF 则返回空字符串。
''' 
 	WORDS.append(str(word.strip(), encoding="utf-8")) #
'''
word以字符串形式中存有1行网页源代码

strip() 方法用于移除字符串头尾指定的字符（默认为空格）或字符序列。
			   注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。

str() 函数将对象转化为适于人阅读的形式。
	  返回一个对象的string格式。
		>>>s = 'RUNOOB'
		>>> str(s)
		'RUNOOB'
		>>> dict = {'runoob': 'runoob.com', 'google': 'google.com'};
		>>> str(dict)
		"{'google': 'google.com', 'runoob': 'runoob.com'}"
		>>>
将word的中的字符串去头尾后以utf-8编码写入WORDS列表末尾
'''

def convert(snippet, phrase):
	class_names = [w.capitalize() for w in 
				   random.sample(WORDS, snippet.count("%%%"))]  
	other_names = random.sample(WORDS, snippet.count("***"))
	'''
	count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
	
	random.sample(p, k)
	从p序列中，随机获取k个元素，生成一个新序列。 sample不改变原来序列。
	
	str.capitalize()将字符串的第一个字母变成大写,其他字母变小写。
	'''
	results = []
	param_names = []

	for i in range(0, snippet.count("@@@")): 
		param_count = random.randint(1, 3) 
		param_names.append(', '.join(
			random.sample(WORDS, param_count))) 
		'''
		join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
	    
	    random.randint(1, 10) 语句的含义是产生1至10（ 包含1与10）的一个随机数（ 整数int型）。
	    				     （参数为整数不可为浮点数否则会报错)
		
		'''
	for sentence in snippet, phrase: # ??????
		result = sentence[:] 
		'''
		列表切片语法未指定索引，返回了整个列表，如此完成了整个列表的复制
		'''

		# fake class names
		for word in class_names:
			result = result.replace("%%%", word, 1) #
			'''
			replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，
			          如果指定第三个参数max，则替换不超过 max 次。
			'''

		# fake other names
		for word in other_names:
			result = result.replace("***", word, 1)

		# fake parameter lists
		for word in param_names:
			result = result.replace("@@@", word, 1)

		results.append(result)

	return results # 返回了一个字符串列表


# keep going until they hit CTRL-D
try: # 
	while True:
		snippets = list(PHRASES.keys())
		'''
		Python3 字典 keys() 方法返回一个可迭代对象，可以使用 list() 来转换为列表。
		注意：Python2.x 是直接返回列表
		'''  
		random.shuffle(snippets) #
		#把序列snippets中的元素顺序打乱。 shuffle直接改变原有的序列

		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASES_FIRST:
				question, answer = answer, question

			print(question)

			input("> ")
			print(f"ANSWER: {answer}\n\n")
except EOFError:
	print("\nBye")
'''
try 语句按照如下方式工作；

首先，执行 try 子句（在关键字 try 和关键字 except 之间的语句）。

如果没有异常发生，忽略 except 子句，try 子句执行后结束。

如果在执行 try 子句的过程中发生了异常，那么 try 子句余下的部分将被忽略。

如果异常的类型和 except 之后的名称相符，那么对应的 except 子句将被执行。

如果一个异常没有与任何的 except 匹配，那么这个异常将会传递给上层的 try 中。

一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。

处理程序将只针对对应的 try 子句中的异常进行处理，而不是其他的 try 的处理程序中的异常
'''