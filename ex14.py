from sys import argv

script, user_name, times = argv 
prompt = 'Answer: '

print(f"hi {user_name}, i'm the {script} script")
print("I'd like to ask you some questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print(f"""
alright, so you said {likes} about liking me.
you live in {lives}.   not sure where that is.
and you have a {computer} computer.      Nice.
you have used me {times} times.         great.	
	""")
