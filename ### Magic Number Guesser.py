### Magic Number Guesser
### DTSC 5501-801 Assignment #2-From Flowchart to Python ###
### Timothy Williams, 9.7.2026

### Objective: Based on the algorithm instructions and flowchart developed from the first assignment, build a program in python
### Which solves the problem based on the proposed solution
### Turn the design into python code and improve on the original solution as needed

### I will post the orginal document with the proposed design and flowchart into the repository

# Measuring Execution Time
import random
import time
begin = time.perf_counter()


# Parameters

low = 1
high = 99

# list of prime numbers from 1 - 99
prime_n = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 
           37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# Search Algorithm
# Input sequence
print("Magic Number Guesser: Input a number and I will try to guess what it is! :)")
n = input("What is your number selection (please choose from 1-99): ", )
n = int(n)
print(n)

# Instructions for Search

g_1 = 50
g_2 = [25, 75]
g_3 = [11, 37, 67, 83]
g_4 = [7, 19, 31, 43, 59, 73, 79, 89]

## Guess #5 will be consist of a series of lists conditional on the fourth guess (g_4)

## Function for guessing numbers

n_g = 1
g = 0
def guess(n_g, g):
    global low, high
    while n_g <= 12:
        if n_g == 1:
            g = g_1
            print("Is this guess higher than the number, lower, or correct?")
            if n < g:
                g = g_2[0]
                print("Lower, guessing ", g)
                n_g += 1
                continue
            elif n > g:
                g = g_2[1]
                print("Higher, guessing ", g)
                n_g += 1
                continue
            elif n == g:
                print(g_1, " is correct!")
            return
        ### Second Guess Sequence
        if n_g == 2 and g == g_2[0]:
            g = g_2[0]
            print("Is this guess higher than the number, lower, or correct?")
            if n < g_2[0]:
                g = g_3[0]
                print("Lower, guessing ", g)
                n_g += 1
                continue
            elif n > g_2[0]:
                g = g_3[1]
                print("Higher, guessing ", g)
                n_g += 1
                continue
            elif n == g_2[0]:
                print("Correct!", g = n)
            return
        if n_g == 2 and g == g_2[1]:
                    g = g_2[1]
                    print("Is this guess higher than the number, lower, or correct?")
                    if n < g_2[1]:
                        g = g_3[2]
                        print("Lower, guessing ", g)
                        n_g += 1
                        continue
                    elif n > g_2[1]:
                        g = g_3[3]
                        print("Higher, guessing ", g)
                        n_g += 1
                        continue
                    elif n == g_2[1]:
                        print(g, " is correct!")
                    return
        ### Third guess sequence
        if n_g == 3 and g == g_3[0]:
                    g = g_3[0]
                    print("Is this guess higher than the number, lower, or correct?")
                    if n < g_3[0]:
                        g = g_4[0]
                        print("Lower, guessing ", g)
                        n_g += 1
                        continue
                    elif n > g_3[0]:
                        g = g_4[1]
                        print("Higher, guessing ", g)
                        n_g += 1
                        continue
                    elif n == g_3[0]:
                        print(g, " is correct!")
                    return
        if n_g == 3 and g == g_3[1]:
                    g = g_3[1]
                    print("Is this guess higher than the number, lower, or correct?")
                    if n < g_3[1]:
                        g = g_4[2]
                        print("Lower, guessing ", g)
                        n_g += 1
                        continue
                    elif n > g_3[1]:
                        g = g_4[3]
                        print("Higher, guessing ", g)
                        n_g += 1
                        continue
                    elif n == g_3[1]:
                        print(g, " is correct!")
                    return
        if n_g == 3 and g == g_3[2]:
                    g = g_3[2]
                    print("Is this guess higher than the number, lower, or correct?")
                    if n < g_3[2]:
                        g = g_4[4]
                        print("Lower, guessing ", g)
                        n_g += 1
                        continue
                    elif n > g_3[2]:
                        g = g_4[5]
                        print("Higher, guessing ", g)
                        n_g += 1
                        continue
                    elif n == g_3[2]:
                        print(g_3[2], " is correct!")
                    return
        if n_g == 3 and g == g_3[3]:
                            g = g_3[3]
                            print("Is this guess higher than the number, lower, or correct?")
                            if n < g_3[3]:
                                g = g_4[6]
                                print("Lower, guessing ", g)
                                n_g += 1
                                continue
                            elif n > g_3[3]:
                                g = g_4[7]
                                print("Higher, guessing ", g)
                                n_g += 1
                                continue
                            elif n == g_3[3]:
                                print(g_3[3], " is correct!")
                            return
        ### Fourth guess sequence
        if n_g == 4 and g == g_4[0]:
                            g = g_4[0]
                            print("Is this guess higher than the number, lower, or correct?")
                            if n < g_4[0]:
                                rand_1 = [1, 2, 3, 4, 5, 6]
                                g = random_g = random.choice(rand_1)
                                print("Lower, guessing ", random_g)
                                n_g += 1
                                continue
                            elif n > g_4[0]:
                                rand_2 = [8, 9, 10]
                                g = random_g = random.choice(rand_2)
                                print("Higher, guessing ", random_g)
                                n_g += 1
                                continue
                            elif n == g_4[0]:
                                print(g_4[0], " is correct!")
                            return
        if n_g == 4 and g == g_4[1]:
                                    g = g_4[1]
                                    print("Is this guess higher than the number, lower, or correct?")
                                    if n < g_4[1]:
                                        rand_3 = [12, 13, 14, 15, 16, 17, 18]
                                        g = random_g = random.choice(rand_3)
                                        print("Lower, guessing ", random_g)
                                        n_g += 1
                                        continue
                                    elif n > g_4[1]:
                                        rand_4 = [20, 21, 22, 23, 24]
                                        g = random_g = random.choice(rand_4)
                                        print("Higher, guessing ", random_g)
                                        n_g += 1
                                        continue
                                    elif n == g_4[1]:
                                        print(g_4[1], " is correct!")
                                    return
        if n_g == 4 and g == g_4[2]:
                                    g = g_4[2]
                                    print("Is this guess higher than the number, lower, or correct?")
                                    if n < g_4[2]:
                                        rand_5 = [26, 27, 28, 29, 30]
                                        g = random_g = random.choice(rand_5)
                                        print("Lower, guessing ", random_g)
                                        n_g += 1
                                        continue
                                    elif n > g_4[2]:
                                        rand_6 = [32, 33, 34, 35, 36]
                                        g = random_g = random.choice(rand_6)
                                        print("Higher, guessing ", random_g)
                                        n_g += 1
                                        continue
                                    elif n == g_4[2]:
                                        print(g_4[2], " is correct!")
                                        print("Terminating guessing algorithm!")
                                    return
        if n_g == 4 and g == g_4[3]:
                                    g = g_4[3]
                                    print("Is this guess higher than the number, lower, or correct?")
                                    if n < g_4[3]:
                                        rand_7 = [38, 39, 40, 41]
                                        g = random_g = random.choice(rand_7)
                                        print("Lower, guessing ", random_g)
                                        n_g += 1
                                        continue
                                    elif n > g_4[3]:
                                        rand_8 = [44, 45, 46, 47, 48, 49]
                                        g = random_g = random.choice(rand_8)
                                        print("Higher, guessing ", random_g)
                                        n_g += 1
                                        continue
                                    elif n == g_4[3]:
                                        print(g_4[3], " is correct!")
                                    return
        if n_g == 4 and g == g_4[4]:
                                    g = g_4[4]
                                    print("Is this guess higher than the number, lower, or correct?")
                                    if n < g_4[4]:
                                        rand_9 = [51, 52, 53, 54, 55, 56, 57, 58]
                                        g = random_g = random.choice(rand_9)
                                        print("Lower, guessing ", random_g)
                                        n_g += 1
                                        continue
                                    elif n > g_4[4]:
                                        rand_10 = [60, 61, 62, 63, 64, 65, 66]
                                        g = random_g = random.choice(rand_10)
                                        print("Higher, guessing ", random_g)
                                        n_g += 1
                                        continue
                                    elif n == g_4[4]:
                                        print(g_4[4], " is correct!")
                                    return
        if n_g == 4 and g == g_4[5]:
                                    g = g_4[5]
                                    print("Is this guess higher than the number, lower, or correct?")
                                    if n < g_4[5]:
                                        rand_11 = [68, 69, 70, 71, 72]
                                        g = random_g = random.choice(rand_11)
                                        print("Lower, guessing ", random_g)
                                        n_g += 1
                                        continue
                                    elif n > g_4[5]:
                                        rand_12 = [74]
                                        g = random_g = random.choice(rand_12)
                                        print("Higher, guessing ", random_g)
                                        n_g += 1
                                        continue
                                    elif n == g_4[5]:
                                        print(g_4[5], " is correct!")
                                    return
        if n_g == 4 and g == g_4[6]:
                                    g = g_4[6]
                                    print("Is this guess higher than the number, lower, or correct?")
                                    if n < g_4[6]:
                                        rand_7 = [76, 77, 78]
                                        g = random_g = random.choice(rand_7)
                                        print("Lower, guessing ", random_g)
                                        n_g += 1
                                        continue
                                    elif n > g_4[6]:
                                        rand_8 = [80, 81, 82]
                                        g = random_g = random.choice(rand_8)
                                        print("Higher, guessing ", random_g)
                                        n_g += 1
                                        continue
                                    elif n == g_4[6]:
                                        print(g_4[6], " is correct!")
                                    return
        if n_g == 4 and g == g_4[7]:
                                    g = g_4[7]
                                    print("Is this guess higher than the number, lower, or correct?")
                                    if n < g_4[7]:
                                        rand_9 = [84, 85, 86, 87, 88]
                                        g = random_g = random.choice(rand_9)
                                        print("Lower, guessing ", random_g)
                                        n_g += 1
                                        continue
                                    elif n > g_4[7]:
                                        rand_10 = [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
                                        g = random_g = random.choice(rand_10)
                                        print("Higher, guessing ", random_g)
                                        n_g += 1
                                        continue
                                    elif n == g_4[7]:
                                        print(g_4[7], " is correct!")
                                    return
    ### Guess until the number is guessed or 10 guesses have been made
        if n_g >= 5:
            print("Is this guess higher than the number, lower, or correct?")

            if n < random_g:
                high = random_g - 1
                print("Lower")
            elif n > random_g:
                low = random_g + 1
                print("Higher")
            else:
                print(random_g, " is correct!")
                return n_g

            random_g = random.randint(low, high)
            g = random_g
            print("Guessing", random_g)
            n_g += 1
            continue
        return n_g
    return n_g


guess(n_g, g)


number_of_guesses = guess(n_g, g)


print("I was able to guess your number in ", number_of_guesses, " guesses!")
end = time.perf_counter()
print("Terminating guessing algorithm!")
print(f"Total runtime is {end - begin}")