filename = input("Please enter file's name: ")

txt = open(filename)

print(f"here is file {filename}: ")
print(txt.read())