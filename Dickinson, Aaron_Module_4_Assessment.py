# Aaron Dickinson
# Module 4 Assessment
# Software Developmet
# Dr. Benjamin Garlington


"""Program 1"""

print("Program 1\n")

def hello():
	"""Prints "Hello World" when called"""
	print("Hello World \n")

#Variable in global scope
x = 42 

def add_a_num():
	"""Adds a variable in the global scope to the one in the local scope and prints the result"""
	
	#Variable in local scope
	y = 7 
	print(x+y)

#Calls to functions
hello()
add_a_num()

"""End of Program 1"""

#Line break between programs
print("\n", "*"*80, "\n") 

"""Program 2"""

print("Program 2\n")

def sum_nums(*args):
	"""Adds all arguments together and returns total"""
	total = 0
	for i in args:
		total += i
	#Converts the total to an integer if possible.
	if float(total).is_integer():
		total = int(total)
	else: 
		pass
	return total

print("This program finds the sum of your numbers.\n")
#Prompts the user for a list of numbers
while True:
	list_of_nums = input("Input your numbers separated by a space: ",)
	try:
		#Converts the string of user numbers into a list of floating point numbers.
		list_of_nums = list_of_nums.split()
		for i in range(len(list_of_nums)):
			list_of_nums[i] = float(list_of_nums[i])
	#Validates user input as numbers and reprompts them if not.
	except ValueError:
		print("\nOne or more of your entries was not an number. Please try again.\n")
	else:
		break

#Calls sum_nums function, saves to new variable, and prints result
sum_of_nums = sum_nums(*list_of_nums)
print(f"\nThe sum of your numbers is: {sum_of_nums}")

#Does the same as sum_nums, but with a reduce() and lambda function
from functools import reduce
total = reduce(lambda x, y: x+y, list_of_nums)
#Converts the total to an integer if possible.
if float(total).is_integer():
	total = int(total)
else: 
	pass
print(f"\nThis is also the sum of your numbers but done with a reduce() and lamdba function: {total}")

#Squares each number, then calls sum_nums to total the squares, and prints result
squared_nums = list(map(lambda num: num**2, list_of_nums))
print(f"\nYour numbers squared and them summed is: {sum_nums(*squared_nums)}")
print("\tThis was only so I could use the map() and list() functions.")

"""End of Program 2"""

# Line break between programs
print("\n", "*"*80, "\n") 

"""Program 3"""

def median(list):
	"""Finds the middle value in a list of numbers. 
	If the list contains an odd number of items, the middle value is returned.
	If the list contains an even number of items, the middle two values are averaged and returned"""
	#Finds if list has odd number of items and returns the middle value
	if len(list) % 2 != 0:
		mid_point = len(list)//2
		median = list[mid_point]
	else:
		#Returns the average of the middle two values if the list contains an even number of items
		mid_point = len(list)//2
		median = (list[mid_point] + list[mid_point -1]) / 2
	#Converts the median to an integer if possible
	if float(median).is_integer():
		median = int(median)
	else: 
		pass
	return(median)

def mode(list):
	"""Returns the value that occures most often in a list.
	In the even of a tie, the first value is returned"""
	#Creates a list of the number of occurances for each value
	occurances = []
	for i in list:
		occurances.append(list.count(i))
	#Finds and returns the value with the maximum number of occurances 
	index_of_max = (occurances.index(max(occurances)))
	mode = list[index_of_max]
	#Converts the mode to an integer if possible
	if float(mode).is_integer():
		mode = int(mode)
	else: 
		pass
	return(mode)
	

def mean(list):
	"""Finds and returns the mean of all the numbers in a list"""
	sum = 0
	for i in list:
		sum += i
	mean = sum/len(list)
	#Converts the mean to an integer if possible
	if float(mean).is_integer():
		mean = int(mean)
	else: 
		pass
	return(mean)

def main():
	print("Program 3\n")
	print("This program will find the mean, median, and mode of your numbers.\n")
	#Prompts the user for a list of numbers
	while True:
		list_of_nums = input("Input your numbers separated by a space: ",)
		try:
			#Converts the string of user numbers into a list of floating point numbers.
			list_of_nums = list_of_nums.split()
			for i in range(len(list_of_nums)):
				list_of_nums[i] = float(list_of_nums[i])
		#Validates user input as numbers and reprompts them if not.
		except ValueError:
			print("\nOne or more of your entries was not an number. Please try again.\n")
		else:
			break
	

	#Calls the mean, median, and mode functions and prints the result
	print("\n")
	print(f"The mean is {mean(list_of_nums)}")
	print(f"The median is {median(list_of_nums)}")
	print(f"The mode is {mode(list_of_nums)}")
	
if __name__ == "__main__":

	#Calls the main function containing calls for mean, median, and mode
	main()

	#Keeps command prompt open when running on windows until you're ready to close
	print("\n")
	input("Press enter to exit.",)

"""End of Program 3"""