from sys import argv

script, filename = argv

print(f"we are going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you want that , hit RETURN. ")

input("?")

print("Opening the file...")
target = open(filename, 'w') 
# 'w' :打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。

print("Truncating the file. goodbye!")
target.truncate() #实际上并不需要，line12已实现此功能


print("now,I'm asking you for three lines.")

line_1 = input("Line 1: ")
line_2 = input("line 2: ")
line_3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line_1)
target.write("\n")
target.write(line_2)
target.write("\n")
target.write(line_3)
target.write("\n")

print("And finally,we close it.")
target.close()