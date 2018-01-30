# Guess the random number

import random 
num = random.randrange(1,10)             # random function is used to generate the random number within range
cnt = 1

user_input = input("Please enter random number between 1 to 10")          #input from user 
while user_input != num:                                                   # if not match than try again
	print ("NOT MATCHED")
	user_input=input("Try again")
	cnt = cnt + 1
	
	if cnt >=6 :                                                   #if count is greater than the given chance than exit
		print ("Game Over")
		exit()
	
print ("--------END------")

print ("MATCH FOUND {0} AFTER : {1}" .format(num, cnt) )
