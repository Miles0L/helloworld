from sys import argv

script, input_file = argv

def print_all(f):
	print(f.read())
# 打印文件f的全部内容

def rewind(f):
	f.seek(0)
# 将光标移动到文件f内容的第一个字符前（开头）

def print_a_line(line_count, f):
	print(line_count, f.readline())
# 打印line_count的值，读取文件f内容的一行，读取出\n后在此处停下，在文件f中写入readline的读取位置

current_file = open(input_file)
# 打开文件input_file并将文件对象赋给current_file

print("First,let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")	

rewind(current_file) # 将光标移动到文件内容的第一个字符前

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)
# 输出行数1并打印在第1个\n前的内容

current_line = current_line + 1
print_a_line(current_line, current_file)
# 输出行数2并打印在第2个\n前的内容

current_line = current_line + 1
print_a_line(current_line, current_file)
# 输出行数3并打印在第3个\n前的内容