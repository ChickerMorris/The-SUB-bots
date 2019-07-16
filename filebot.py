#Chat bot
#author Zachary Morris
print("Hello, and welcome")

#list for user, pass, and cmds
user_list = [
	"krj5602",
	"user150",
	"area51bot"
]

passlist = [
	"56trpd",
	"whydoesthiswork",
	"password1"
]

cmdlist = [
	"search",
	"file"
]


while True:
	print("Please Sing In:")
	username = raw_input("Username:")
	password = raw_input("Password:")

	if username in user_list and password in passlist:
		print("Welcome " + username + " please enter a command")
		print(cmdlist)
		cmd = raw_input("Which command?")
		if cmd == "search" or "file":
			fileget = raw_input("which file do you want?")
			if fileget == "the file":
				print("this is the file you want: https://bit.ly/30xnnog")
	else:
		print("Incorrect")
