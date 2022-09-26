"""Aaron Dickinson
   Module 3 Assessment
   Software Developmet
   Dr. Benjamin Garlington"""



'''Program 1: Checks if a given number is even or odd'''

# #Gets a number from the user and casts as interger.
user_num = int(input("Enter a number: "))

#Checks if the number is even and prints result
if user_num % 2 == 0:
    print(f"\n{user_num} is an even number! \n")
else:
    print(f"\n{user_num} is an odd number! \n")

'''End of program 1'''



print("*"*80, "\n") # Line break between programs



'''Program 2: Finds the average of a list of provided numbers'''

# Creates an empty list and a variable for the running total
user_nums = []
total = 0

# Gets the number of numbers to be aveaged and casts as an interger
count = int(input("How many numbers are you averaging? "))

# Gets the users numbers to be averaged and adds them to the list
user_nums.append(float(input("What is your first number? ")))
for i in range (count-1):
    user_nums.append(float(input("What is your next number? ")))

# Finds the total of all the numbers
for num in user_nums:
    total += num

# Calculates and prints the average
average = total / count
print(f"\nThe average of your numbers was {average} \n")

'''End of program 2'''



print("*"*80, "\n") # Line break between programs



'''Program 3: Finds the total distance travled by a ball bounced N times of a given bounciness index'''

# Collects user input about the ball
height = float(input("Enter the height from which the ball is dropped: "))
bounciness_index = float(input("Enter the bounciness index of the ball: "))
num_of_bounces = int(input("Enter the number of times the ball is allowed to continue bouncing: "))

#Finds the total distance travled by the ball and prints the total
distance = 0
for bounces in range(num_of_bounces):
    distance += height
    height *= bounciness_index
    distance += height

print(f"\nTotal distance traveled is: {distance} units. \n")

'''End of program 3'''

input("Press enter to exit")