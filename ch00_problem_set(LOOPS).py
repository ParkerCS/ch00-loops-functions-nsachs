#19/22
# LOOPS (22pts TOTAL)

# PROBLEM 1 (Fibonacci - 4pts)
## The Fibonacci sequence is a sequence of numbers that starts with 1, followed by 1 again.
# Every next number is the sum of the two previous numbers.
# I.e., the sequence starts with 1, 1, 2, 3, 5, 8, 13, 21,...
# Write a program that calculates and prints the Fibonacci sequence
# until the numbers get higher than 1000.
a = 1
b = 1

while a < 1000 and b < 1000:
    print(a) # This does two steps each time through loop
    print(b)
    a += b
    b += a
print()


# PROBLEM 2 (Number Guessing Game - 6pts)
# Write a program that takes a random integer between 1 and 1000
# The program then asks the user to guess the number.
# After every guess, the program will say either “Lower”
# if the number it took is lower, “Higher” if the number it took is higher,
# and “You guessed it!” if the number it took is equal to the number
# It might be wise, for testing purposes, to also display the number that the
# program randomly picks, until you are sure that the program works correctly
import random

computer = random.randrange(1,1001)
print(computer)

done = False
while not done:
    guess = int(input("Enter a number between 1 and 1000: "))
    if guess > computer:
        print("Lower")
    elif guess < computer:
        print("Higher")
    elif guess == computer:
        done = True
print("You guessed it!")
print()

# PROBLEM 3 (Dice Hi-Low - 6pts)
# You roll five six-sided dice, one by one.
# How big is the probability that the value of each die
# is greater than or equal to the value of the previous die that you rolled?
# For example, the sequence “1, 1, 4, 4, 6” is a success,
# but “1, 1, 4, 3, 6” is not. Determine the
# probability of success using a simulation of a large number of trials.
c = [0]
percent_success = 0
for i in range(10000):
    x = [0]
    for i in range(1, 6):
        y = random.randrange(1, 7)/ i
        x.append(y * i)
        if y * i < x[i - 1]:
            percent_success += 1
    c.append(x)

percent_success /= 50000
print("The likelihood that the value previously rolled is lower every time is: ", round(percent_success * 100, 2), "%.")

print()

# Lee - This is very much like what Franny submitted.  Same misunderstandings.  Take care if you are working together.  This doesn't really do a lot to solve this problem.  You divide percent success by 50000 (why?).  You divide by i in the loop (why?).  You build a list, but don't use it.  See franny's for solution.(-3)

# PROBLEM 4 (Number Puzzler - 6pts)
# A, B, C, and D are all different digits.
# The number DCBA is equal to 4 times the number ABCD.
# What are the digits?
# Note: to make ABCD and DCBA conventional numbers, neither A nor D can be zero.
# Use a quadruple-nested loop to solve.
for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            for d in range(1, 10):
                if int(str(d) + str(c) + str(b) + str(a)) == 4 * int(str(a) + str(b) + str(c) + str(d)):
                    print(a, b, c, d)

