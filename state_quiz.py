capitals_dict = {
'AndhraPradesh' : 'Hyderabad',
'ArunachalPradesh' : 'Itanagar',
'Assam' : 'Dispur',
'Bihar' : 'Patna',
'Goa' : 'Panaji',
'Gujarat' : 'Gandhinagar',
'Haryana' : 'Chandigarh',
'HimachalPradesh' : 'Shimla',
'JammuKashmir' : 'Srinagar',
'Karnataka' : 'Bangalooru',
'Kerala' : 'Thiruvananthapuram',
'MadhyaPradesh' : 'Bhopal',
'Maharashtra' : 'Mumbai',
'Manipur' : 'Imphal',
'Meghalaya' : 'Shillong',
'Mizoram' : 'Aizawl',
'Nagaland' : 'Kohima',
'Orissa' : 'Bhubaneswar',
'Punjab' : 'Chandigarh',
'Rajasthan' : 'Jaipur',
'Sikkim' : 'Gangtok',
'TamilNadu' : 'Chennai',
'Tripura' : 'Agartala',
'UttarPradesh' : 'Lucknow',
'WestBengal' : 'Kolkata',
'Chhattisgarh' : 'Raipur',
'Uttarakhand' : 'Dehradun',
'Jharkhand' : 'Ranchi',
'Telangana' : 'Hyderabad',
}

import random

states = list (capitals_dict.keys())
ques = int (input("Enter the number of questions to be asked between 1 and 28 : "))
#ques = raw_input("Enter the number of questions to be asked between 1 and 28 : ")
if ques>=1 and ques <= 28:
    correct_ans = 0

    for i in range(0,ques):
	    state = random.choice(states)
	    capital = capitals_dict[state]
	    capital = capital.lower()
	    #capital_guess = input("What is the capital of " + state + "?")
	    capital_guess = raw_input("What is the capital of " + state + "?")
	    capital_guess = capital_guess.lower()
	
	    if capital_guess == capital:
		    print("You Got it Correct! Good Job")
		    correct_ans = correct_ans + 1
	    else:
		    print("Its Wrong!")
		    print("The correct answer is %s" %capital)
    
	
    print ("Quiz Completed")
    print ("Total questions asked %i " %ques)
    print ("Number of questions answered correctly  %i " %correct_ans)
    percent = float(correct_ans)/ques * 100
    percent = str(round(percent, 2))
    print ("Your Percentage of this quiz is %s " %percent)
	
else:
    print("Wrong Choice")
