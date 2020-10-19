# 复制文件内容到另一个文件
from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file) # 打开from_file文件并将文件对象传给in_file
indata = in_file.read()	# 读取in_file所有内容并传入indata

# print(f"The input file is {len(indata)} bytes long")

# print(f"Does the output file exist ?{exists(to_file)}")
# print("Ready, hit RETURN to continue, CTRL-C to abort")
# input('> ')

out_file = open(to_file, 'w') # 打开或创建to_file文件并将文件对象传给out_file
out_file.write(indata) # 将indata的内容写入out_file

# print("Alright, all done.")

out_file.close() # 关闭 out_file的文件对象
in_file.close() # 关闭 in_file的文件对象