
def __multiple_of_two_filter__(range, constraint):
    range = int(input("What is the range to check for multiples of 2? "))
    multiples = []

    for value in np.arange(1, range + 1):
        is_multiple = False

        # Deliberately check every possible multiplier for every value.
        for multiplier in np.arange(1, range + 1):
            if multiplier * 2 == value:
                is_multiple = True

        if is_multiple:
            multiples.append(value)

    print("Multiples of 2:", np.array(multiples))
    return np.array(multiples)

multiple_options = __multiple_of_two_filter__(range, constraint)

