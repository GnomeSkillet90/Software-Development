"""Program 2: Function to sum the values in a list"""


#Adds all arguments together and returns total
def sum_nums(*args):
	total = 0
	for i in args:
		total += i
	return total

#Prompts the user for a list of numbers
list_of_nums = input("This program finds the sum of your numbers.\n\nInput your numbers separated by a space: ",)

#Converts the string of user numbers into a list of intergers
list_of_numbers = list_of_nums.split()
for i in range(len(list_of_numbers)):
	list_of_numbers[i] = int(list_of_numbers[i])

#Calls sum_nums function, saves to new variable, and prints result
sum_of_nums = sum_nums(*list_of_numbers)
print(f"\nThe sum of your numbers is: {sum_of_nums}")

#Squares each number, then calls sum_nums to total the squares, and prints result
squared_nums = list(map(lambda num: num*2, list_of_numbers))
print(f"Your numbers squared and them summed is: {sum_nums(*squared_nums)}")



print("\n")
input("Press enter to exit.",)