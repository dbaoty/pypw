# TODO:
# fix up helper function

import random
import string
import sys
import pyperclip

def printHelp() -> None:
    print('HELP function')
    exit(0)

def copyToClipboard(pw: str) -> None:
    if pyperclip:
        pyperclip.copy(pw)
    else:
        print("python module 'pyperclip' could not be found.")
        exit()

def validateArguments(l: list) -> list:
    """
    validateArguments performs length-wise and logic checks on sys.argv arguments.

    :param list: list of arguments from sys.argv

    :return: returns the list of arguments if all arguments are determined to be valid.
    """
    if len(l) > 3: printHelp()

    for _ in l[1:]:
        if _ > 1 or _ < 0:
            printHelp()

    return list

def generatePassword(length: int = 8, capitalization: int = 1, special_chars: int = 1) -> str:
    """
    generatePassword takes 3 positional arguments from the command line and generates a 
    secure password using the operating systems' version of urandom.

    :param length: defaults to 8 character length
    :param capitalization: enable capital letters in password.
    :param special_chars: enable special characters in password.

    :return: returns a string of specified length and configuration based on value given 
    to the capitalization and special character arguments.
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
    l = [int(i) for i in sys.argv[1:]]

    pw = generatePassword(*l)
    print(pw)

    if 'pyperclip' in sys.modules:
        conf = input('save new password to clipboard? (y/n): ')
        if conf.upper() == "Y":
            copyToClipboard(pw)
    else:
        print("python module 'pyperclip' could not be found.")
