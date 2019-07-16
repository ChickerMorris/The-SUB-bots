#Chat bot
#author Zachary Morris
import time

print("Hello, and welcome")
time.sleep(3)
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

filelist = [
	"the file",
	"fileB56",
	"WT_"
]

#the loop
while True:
	print("Please Sing In:")
	username = raw_input("Username:")
	password = raw_input("Password:")

	#checks to see if the username and password is right
	if username in user_list and password in passlist:
		print("Welcome " + username + " please enter a command")
		print(cmdlist)
		#checks to see what type of command they want
		cmd = raw_input("Which command?")
		#what happens if they select file
		if cmd == "file":
			print(filelist)
			fileget = raw_input("which file do you want?")
			if fileget == "the file":
				print("this is the file you want: https://bit.ly/30xnnog")
			if cmd == "fileB56"
				time.sleep(3)
				print("Here you go: https://bit.ly/2y1Yzc7")
			if fileget == "WT_"
				time.sleep(3)
				print("Here you go: https://bit.ly/2KcFV54")
		else:
			print("anything else?")
		#what happens if they select search
		if cmd == "search":
			result = raw_input("what do you want to search?")
			if result == "The Creator":
				print("My Creator is a person that which you got this code from")
			if result =="fortnite"
				print("Nah Fam")
		else:
			print("I am sorry I do not know that. If you want something different go here: https://google.com")

	else:
		print("Incorrect")
