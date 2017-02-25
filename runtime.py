# I found this chart that may be helpful for others. I didn't know if it was ok to post it
# on slack since we're in the middle of an assessment weekend:
#  https://wiki.python.org/moin/TimeComplexity



def string_compare(s1, s2):
    """Given two strings, figure out if they are exactly the same (without using ==).

    Put runtime here:
    -----------------
    [     O(n) - checking len of list should be O(1), for loop depends on len list and
    so would be O(n) where n is the length of the list        ]


    """

    if len(s1) != len(s2):
        return False

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True


def has_exotic_animals(animals):
    """Determine whether a list of animals contains exotic animals.

    Put runtime here:
    -----------------
    [    O(n) - for loop       (I think even though you do the for loop twice, the 2x is
    disregarded since it's not an exponent and the loops aren't nested)    ]

    """

    if "hippo" in animals or "platpypus" in animals:
        return True
    else:
        return False


def sum_zero_1(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [       O(n) - because the set is given as O(n), iterating x in a set is O(1),
    iterating -x in a set should also be O(1), and appending a list is O(1)        ]

    """

    result = []

    # Hint: the following line, "s = set(numbers)", is O(n) ---
    # we'll learn exactly why later
    s = set(numbers)

    for x in s:
        if -x in s:
            result.append([-x, x])

    return result


def sum_zero_2(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [      O(n**2) - because this is a nested for loop         ]

    """

    result = []

    for x in numbers:
        for y in numbers:
            if x == -y:
                result.append((x, y))
    return result


def sum_zero_3(numbers):
    """Find pairs of integers that sum to zero.

    This version gets rid of duplicates (it won't add (1, -1) if (-1, 1) already there.

    Put runtime here:
    -----------------
    [     O(n**3)  - nested for loop is O(n**2) and then checking the result list is
    another O(n)           ]

    """

    result = []

    for x in numbers:
        for y in numbers:
            if x == -y and (y, x) not in result:
                result.append((x, y))
    return result
