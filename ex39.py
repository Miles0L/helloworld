# creat a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# Creat a basic set of states and some cities in them
cities = {
	'CA': 'San francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan abbreviation is: ", states['Michigan'])
print("Florida abbreviation is: ", states['Florida'])

# do it by using the state the cities dict
print("-" * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print("-" * 10)
for state, abbrev in list(states.items()):
	"""
	list()： list() 方法用于将元组或字符串转换为列表。
	
	注：元组与列表是非常类似的，区别在于元组的元素值不能修改，元组是放在括号中，列表是放于方括号中。
	
	items(): 字典 items() 方法以列表返回可遍历的(键, 值) 元组数组。
			>>> dict = {'name' : 'penny', 'age' : 47 }
			>>> dict.items()
			dict_items([('name', 'penny'), ('age', 47)])
	
	list(dict.items())返回： [('name', 'penny'),('age', 47)]
	for循环 ： 每一次循环从列表中拿出一个元组，将其中元素分发给state 和abbrev
	"""
	print(f"{state} is abbreviated {abbrev}")

# print every city in state 
print("-" * 10)
for abbrev, city in list(cities.items()):
	print(f"{abbrev} has the city {city}")
	
# now do both at the same time
print("-" * 10)
for state, abbrev in list(states.items()):
	print(f"{state} state is abbreviated {abbrev}")
	print(f"and has city {cities[abbrev]}")

print('-' * 10)

# safely get a abbreviation by state that might not be there
state = states.get('Texas')
"""
get():返回指定键的值，如果键不在字典中返回默认值 None 或者指定的默认值。
"""
if not state: # not state 将state的值变为True
	print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")