#!/usr/bin/env python3

import random
import string
import sys

# TODO:
    # read values from command line
    # fix up helper function
    # autocopy password to clipboard prompt

def printHelp() -> None:
    print('HELP function')
    exit()

def generatePassword(length: int = 8, capitalization: int = 1, special_chars: int = 1) -> str:
    """
    generatePassword takes 3 positional arguments from the command line and generates a secure password using the operating systems' version of urandom.

    :param length: defaults to a length of an 8 character password.
    :param capitalization: allow capital letters in password.
    :param special_chars: allow special characters in password.
    :return: returns a string of specified length and configuration based on value given to the capitalization and special character arguments.
    """ 

    if capitalization:
        pool = string.ascii_lowercase + string.digits + string.ascii_uppercase
    else:
        pool = string.ascii_lowercase + string.digits

    if special_chars:
        sc_pool = '!@#$%^&*'
        pool += sc_pool

    rng = random.SystemRandom()
    temp = ''
    while len(temp) < length:
        temp += rng.choice(pool)

    return temp

if __name__ == "__main__":
    lst = [int(i) for i in sys.argv[1:]]
    if len(lst) > 3: printHelp()

    for l in lst[1:]:
        if l > 1 or l < 0:
            printHelp()

    print(generatePassword(*lst))