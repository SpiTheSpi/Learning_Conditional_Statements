
# if condition: statements to execute
# else: statements to execute 

#print('Hello')
# print('World') #This will show an indentation error, since they only indent on blocs of code.



# Section 1.0
'''
a = 10
b = 9
if a == b:
	print('a is equal to b') # If it is true, then it will execute/ print this statement.
else:
	print('a is not equal to b') # If the executed code is false, then it will print this instead.
'''



# Section 1.1
'''
# If written like C, but this will show up as an error.
# Programming languages like C can have as many indentations as you want, but Python requires a specific/ same indentation to group properly.
# For Python, you can group your code with the same amount of spaces, or same amount of tabs for each line of code you are trying to group for the indentation you want.
# If you use a specific type of indentation, then you need to STICK TO THAT INDENTATION 
# (i.e: Can't use spaces for one line of code that looks like the tabbed indentation on the next line of code.)
if(a == b){
    print('a is equal to b')
}
else{
    print('a is not equal to b')
}
'''



# Section 1.2
'''
a = 10
b = 10
result = a == b
if result:
    print('a is equal to b')
    print('I have confirmed this.')
else:
    print('a is not equal to b')
    print('Done')
'''



# Section 1.3 
'''
# This section of code is just like section 1.2.
# Check the differences on what it executes.
a = 10
b = 10
result = a == b
if result == False:
    print('a is equal to b')
    print('I have confirmed this.')
else:
    print('a is not equal to b')
    print('Done')
'''



# Section 1.4
'''
dog_name = 'Daisy'
dog_gender = 'Female'
dog_age = 5 #any dog younger than 2 years is a puppy.
print('My dog name is', dog_name)
if dog_gender == 'Male':
    print('He is a male')
else:
    print('She is a female')
if dog_gender == 'Male':
	if dog_age < 2:
		print('He is a puppy')
	else:
		print('He is an adult')
else:
	if dog_age < 2:
		print('She is a puppy')
	else:
		print('She is an adult.')
'''



# Section 1.4.1
'''
# Here, we are going to use 'elif' or "else if" statements in looping code.
dog_name = 'Daisy'
# Any dog younger than 2 years is a puppy.
# Any dog between 2 and 5 is young.
# Any dog between 5 and 10 is adult.
# Older than that is old. 
dog_age = 1 #Change the number here to change the outcome of the statements that get printed, "puppy, young, adult, old" will be printed depending on the number you changed.
print('My dog name is', dog_name)
if dog_age < 2:
    print('Puppy')
elif dog_age < 5:
    print('Young')
elif dog_age < 10:
    print('Adult')
else:
    print('Old')
'''



# Section 1.5
'''
# Understanding "and" and "or" conditions w/ Python.
# "and" condition needs both to execute, while "or" needs one or the other to be acceptable in order to execute.
a = 10
b = 10
c = 5
d = 7
if a == b or c == d: #replace the "and" or "or" condition with either one of the "and" or "or" conditions to understand how this simple function works.
    print('Ok')
else:
    print('Bad.')
'''



# Free Style

print("Caesar King| So... how was the grocery shopping?")
print('Caesar Gives you a sparkling look in her eyes while looking at you, and at the grocery bags you bring back home.')

Food_A = {'Cost': 1.00, 'Name': 'Apples', 'Amount': 1}
Food_B = {'Cost': 1.25, 'Name': 'Bread', 'Amount': 1}
Food_C = {'Cost': .70, 'Name': 'Cilantro', 'Amount': 1}

Grocery_Item_Count = int(Food_A['Amount']) * 5 + int(Food_B['Amount']) * 10 + int(Food_C['Amount']) * 1
Grocery_Total_Spent = float(Food_A['Cost']) * 5 + float(Food_B['Cost']) * 10 + float(Food_C['Cost']) * 1
#print(Grocery_Item_Count) # This gives the total amount of how many groceries you have.
#print(Grocery_Total_Spent) # This gives total amount of how much money spent at Groceries.
Caesar_Wallet_Total = -50 # Change this number to get a new response dependent on how much money you "overspent", hahaha.
New_Caesar_Wallet_Total = Caesar_Wallet_Total - Grocery_Total_Spent

if New_Caesar_Wallet_Total == 0:
    print("Caesar King| We spent all of our spare change perfectly! Nice! *Smiles with eyes closed*")
elif New_Caesar_Wallet_Total < -5.00 and New_Caesar_Wallet_Total >= -9.99: # If you overspend and have a balance between -5.00 and -9.99, print this.
        print("Caesar King| Oh no, we overspent hun'! We gotta refund some items back! We only have $", round(New_Caesar_Wallet_Total, 3), "left!")
elif New_Caesar_Wallet_Total < -10.00 and New_Caesar_Wallet_Total >= -99.99: # If you overspend and have a balance between -10.00 and -99.99, print this.
		print("Caesar King| We might've added a little too much to the list... ehehe, my bad! We only have $", round(New_Caesar_Wallet_Total, 3), "left!")
elif New_Caesar_Wallet_Total <= -100.00:
        print("Caesar King| What's wrong with us... How could we be so dumb. *Face Palms* We only have $", round(New_Caesar_Wallet_Total, 3), "left!")
else:
    print("Caesar King| Ah, we have some spare change! Good thing we didn't overspend! We only have $", round(New_Caesar_Wallet_Total, 3), "left by the way!")
