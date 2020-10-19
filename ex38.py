ten_things = "Apples Oranges Crows Telephone Light Sugar" # 字符串

print("Wait there are not 10 things in that list. let's fix that.")

stuff = ten_things.split(' ') # 返回分割后的字符串列表，就像more_stuff。
more_stuff = ["Day", "Night", "Song", "Frisbee",
			  "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10: # len()返回对象（字符、列表、元组等）长度或项目个数。
	next_one = more_stuff.pop() # 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
	print("Adding: ",next_one)
	stuff.append(next_one) # append() 方法用于在列表末尾添加新的对象。
	print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff)) # 返回通过 指定字符 连接 序列中元素 后生成的 新字符串。
print('#'.join(stuff[3:5])) # stuff[3:5] 切片，从基数为3的元素开始取值到基数为5的元素 前 停止，即第四个和第五个元素