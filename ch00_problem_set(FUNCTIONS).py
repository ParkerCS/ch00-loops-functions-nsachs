#SECTION 2 - FUNCTIONS (20PTS TOTAL)

#PROBLEM 1 (Length of String - 3pts)
# Make a function which asks the user to enter a string, then prints the length of that string.
# You will need to use the input() function.
# Make a call to that function
def length(string):
    print(len(string))

length(input("Enter some words: "))

print()

# PROBLEM 2 (Pythagorean theorem - 4pts)
# The Pythagorean theorem states that of a right triangle, the square of the
# length of the diagonal side is equal to the sum of the squares of the lengths
# of the other two sides (or a^2 + b^2 = c^2).
# Write a program that asks the user for the lengths of the two sides that meet at a right angle.
# Then calculate the length of the third side, and display it in a nicely formatted way.
# You may ignore the fact that the user can enter negative or zero lengths for the sides.
def triangle(a, b):
    c = (int(a) ** 2 + int(b) ** 2) ** 0.5
    print("The length of the third side is: ", c)

triangle(int(input("Enter length of side 1: ")), input("Enter length of side 2: "))

print()

# PROBLEM 3 (Biggest, smallest, average - 4pts)
# Make a function to ask the user to enter three numbers.
# Then print the largest, the smallest, and their average, rounded to 2 decimals.
# Display the answers in a "nicely" formatted way.
# Make a call to your function.
def sequence(first, second, third):

    if first >= second and first >= third:
        print(first, "is the largest number.")
    elif second >= first and second >= third:
        print(second, "is the largest number.")
    else:
        print(third, "is the largest number.")

    if first <= second and first <= third:
        print(second, "is the smallest number.")
    elif second <= first and second <= third:
        print(second, "is the smallest number.")
    else:
        print(third, "is the smallest number.")

    average = round((first + second + third)/3, 2)
    print("The average of the numbers is", average)

sequence(int(input("Enter a number: ")), int(input("Enter a number: ")), int(input("Enter a number: ")))

print()

# PROBLEM 4 (e to the... - 3pts)
# Calculate the value of e (from the math library) to the power of -1, 0, 1, 2, and 3.
# display the results, with 5 decimals, in a nicely formatted manner.
import math

def find(x):
    solution = math.e ** x
    print(round(solution,5))

find(-1)
find(0)
find(1)
find(2)
find(3)
print()
# PROBLEM 5 (Random int - 3pts)
# Generate a random integer between 1 and 10 (1 and 10 both included),
# but only use the random() function (randrange is not allowed here)
import random

def integer(k):
    k *= 10
    if k < 1:
        k +=1
    print(round(k))

integer(random.random())

print()


# PROBLEM 6 (add me, multiply me - 3pts)
# Make a function which takes in two integers and RETURNS their sum AND their product.
def calculator(first_number, second_number):
    return first_number + second_number, first_number * second_number

print(calculator(int(input("Enter a number: ")),int(input("Enter another number: "))))