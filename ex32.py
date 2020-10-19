the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count: # for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
	print(f"This is count {number}")

# same as above
for fruit in fruits:
	print(f"A fruit of type :{fruit}")

# Also we can go through mixed lists too
# notice we have to use {} since we don't konw what's in it 
for i in change:
	print(f"I got {i}")

# We can also build lists,first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0,6): 
'''
Python3 range() 函数返回的是一个可迭代对象（类型是对象），而不是列表类型， 所以打印的时候不会打印列表。

Python3 list() 函数是对象迭代器，可以把range()返回的可迭代对象转为一个列表，返回的变量类型为列表。

Python2 range() 函数返回的是列表。

range(stop)
range(start, stop[, step])
参数说明：

start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
'''
	print(f"Adding {i} to the list.")
	# append is a function that lists understand
	elements.append(i)

# now we can print them out too
for i in elements:
	print(f"Element was: {i}")


'''
通过序列索引迭代
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print('当前水果 :', fruits[index])
 
print("Good bye!")
'''