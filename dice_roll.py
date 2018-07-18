import random

flag = "yes"

while (flag == "yes" or flag == "y"):
    input_num = int (input("Enter any number 1 and 6 : "))
    #input_num = int (raw_input("Enter any number 1 and 6 : "))
    if input_num>=1 and input_num <=6:
        print("Dice started rolling....")
        rolled_num=random.randint(1,6)
        print("Dice Rolled and the result is %d" % (rolled_num))

        if input_num == rolled_num:
            print("You Win....")
        else:
            print ("You Lose...")

    else:
        print("wrong Choice")
    
    input_again = raw_input("You want to roll it again? (yes/no)")
    input_again = input_again.lower()
    flag = input_again
	
print ("Game Over...")
