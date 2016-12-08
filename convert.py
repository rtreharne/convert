import numerals
import sys
import re

# TODO function to decide input statment type
# e.g. info or query

def inputType(string):
    queryRegex = re.compile(r'(how|much|many|\?)')
    try:
        if queryRegex.search(string).group():
            return 'query'
    except:
        return None

def extractInfo(string):
    # split string on 'is'
    splitStr = string.split('is')
    return splitStr




# TODO function to learn from info statement

if __name__ == "__main__":

    inputString = input('Please input here: ')
    if inputType(inputString):
        print(extractInfo(inputString))

