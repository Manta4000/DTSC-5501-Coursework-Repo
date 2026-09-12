### Magic number guessing algorithm based on initial testing and experimentation
### Will deploy Sieve of Erasthones after using quartile range calculations instead of brute force
### This was made since I can't hard code a lot of if statements for more than 100 numbers, let alone 10000

### First Stage -- Quartile Determination
import numpy as np
import random as random
import time

constraint = 0.
print("Play the magic number game! Please input your magic number and I will try to guess, all qualitative answers in lowercase please and thank you! :)")
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
    return options_list

options = __quartileRange__(range, constraint)

### Second & third stages-- Sieve of Erasthones // finding all prime numbers in remaining solution set for decimination

p = 2
non = []

def __sieve__(p, n, non):
    maximum = int(np.max(options))
    # Eliminate multiples of 2 and 3 before checking the remaining primes.
    __mask = (options >= 2) & (options % 2 != 0) & (options % 3 != 0)
    __mask |= np.isin(options, [2, 3])
    divisor = 2

    while divisor * divisor <= maximum:
        __mask &= (options % divisor != 0) | (options == divisor)
        divisor += 1

    prime_options = options[__mask | (options == n)]
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


def __multiple_filter__(upper_bound, factor):
    upper_bound = int(upper_bound)
    factor = int(factor)

    if factor <= 0:
        raise ValueError("factor must be a positive integer")

    # Test multiples of two and three together, without testing duplicates.
    multiples = np.arange(1, upper_bound + 1)
    candidates = multiples[(multiples % 2 == 0) | (multiples % 3 == 0)]
    guesses = 0

    while candidates.size:
        guess_index = len(candidates) // 2
        guess = int(candidates[guess_index])
        guesses += 1

        if guesses % 10 == 0:
            correct = input(f"Is {guess} your number? (yes/no) ").strip().lower()
            if correct == "yes":
                print("The number is", guess, "and I guessed it in", guesses, "guesses!")
                return guess

        if n == guess:
            print("The number is", guess, "and I guessed it in", guesses, "guesses!")
            return guess
        elif n < guess:
            # Continue through every candidate lower than this guess.
            candidates = candidates[:guess_index]
        else:
            # Continue through every candidate higher than this guess.
            candidates = candidates[guess_index + 1:]

    print("The magic number was not a multiple of two or three.")
    return None

begin = time.perf_counter()
multiple_of_two = __multiple_filter__(100, 2)
multiple_of_three = __multiple_filter__(100, 3)
end = time.perf_counter()
print(f"Total runtime is {end - begin}")
