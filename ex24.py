print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("---------------")
print(poem)
print("---------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# this is another way to format a string
print("With a start point of: {}".format(start_point))
# It is just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

'''
Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。

基本语法是通过 {} 和 : 来代替以前的 % 。

format 函数可以接受不限个参数，位置可以不按顺序。

实例
	>>>"{} {}".format("hello", "world")    # 不设置指定位置，按默认顺序
	'hello world'
	 
	>>> "{0} {1}".format("hello", "world")  # 设置指定位置
	'hello world'
	 
	>>> "{1} {0} {1}".format("hello", "world")  # 设置指定位置
	'world hello world'

也可以设置参数：
	print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
	 
	# 通过字典设置参数
	site = {"name": "菜鸟教程", "url": "www.runoob.com"}
	print("网站名：{name}, 地址 {url}".format(**site))
	 
	# 通过列表索引设置参数
	my_list = ['菜鸟教程', 'www.runoob.com']
	print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的
'''