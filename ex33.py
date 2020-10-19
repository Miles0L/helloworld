i = 0
numbers = []

while i < 6:
	print(f"At the top i is {i}")
	numbers.append(i)

	i = i + 1
	print("Numbers now: ", numbers)
	print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers: # for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
	print(num)