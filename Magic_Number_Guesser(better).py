### Second generation of magic number guessing algorithm based on feedback
### Will deploy Sieve of Erasthones after using quartile range calculations instead of brute force
### This was made since I can't hard code a lot of if statements for more than 100 numbers, let alone 10000

### First Stage -- Quartile Determination
import numpy as np
import random as random
import time

constraint = 0.

n = int(input("What is your magic number? "))

def __quartileRange__(range, constraint):
    range = int(input("What is the range for guesses? ", ))
    constraint = 0.5*range
    whichQuartile = input("Is the number higher or lower than "f"{constraint}? """)
    if whichQuartile == "higher":
        higher_q = 0.75*range
        whichQuartile1 = input("Is the number higher or lower than "f"{higher_q}? """)

        if whichQuartile1 == "higher":
            options = [0.75*range, range]
        elif whichQuartile1 == "lower":
            options = [0.5*range,0.75*range]
        else:
            return

    elif whichQuartile == "lower":
        lower_q = 0.25*range
        whichQuartile = input("Is the number higher or lower than "f"{lower_q}? """)
        if whichQuartile == "higher":
            options = [0.25*range,0.5*range]
        elif whichQuartile == "lower":
            options = [1,0.25*range]
        else:
            return
    else:
        return

    options = [int(options[0]), int(options[1])]
    options_list = np.arange(options[0], options[1] + 1)
    if range <= 100:
        print(options_list)
    elif range > 100:
        print(options_list[0], np.max(options_list)) ## In the event that the range is really large, I only need the beginning and end
    return options_list

options = __quartileRange__(range, constraint)

### Second & third stages-- Sieve of Erasthones // finding all prime numbers in remaining solution set for decimination

p = 2
non = []

def __sieve__(p, n, non):
    maximum = int(np.max(options))
    __mask = options >= 2
    divisor = 2

    while divisor * divisor <= maximum:
        __mask &= (options % divisor != 0) | (options == divisor)
        divisor += 1

    prime_options = options[__mask | (options == n)]
    print(prime_options)
    return prime_options

        
prime_options = __sieve__(p, n, non)

### Fourth stage -- Use remaining prime number values for continued filtering // actual guessing stage

num = ""
prime = []
def __prime_filter(num, prime, constraint):
    g_count = 0
    candidates = np.array(prime, dtype=int)

    while candidates.size:
        guess_index = len(candidates) // 2
        constraint = int(candidates[guess_index])
        g_count += 1

        if n == constraint:
            print("Great! The magic number is", constraint, "and I guessed it in", g_count, "guesses!")
            return g_count
        elif n > constraint:
            candidates = candidates[guess_index + 1:]
        else:
            candidates = candidates[:guess_index]

    print("The magic number was not in the candidate list.")
    return g_count

begin = time.perf_counter()

__prime_filter(num, prime_options, constraint)

end = time.perf_counter()
print(f"Total runtime is {end - begin}")
print("Program terminated.")