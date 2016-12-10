import numerals
import re
import pprint
from gobble import gobble

def isQuestion(string):
    queryRegex = re.compile(r'(how|much|many|\?)')
    try:
        if queryRegex.search(string).group():
            return True
    except:
        return False

def extractInfo(string, action='learn'):
    # split string on ' is '
    string = string.strip('?')
    splitStr = string.split(' is ')
    keyWords = splitStr[0].split(' ')
    keyVals = splitStr[1].split(' ')
    if len(keyWords) == 1 and len(keyVals) == 1:
        checkGobble(keyWords[0], keyVals[0])
    else:
        return learnOrCalculate(keyWords, keyVals, action)



def learnOrCalculate(keyWords, keyVals, action):
    if action == 'calculate':
        keyWords = keyVals
    else:
        value = int(keyVals[0])

    roman = ''

    for item in keyWords:
        if item[0].islower():
            roman += gobble[item]
        if item[0].isupper():
            multKey = item
            if action == 'learn':
                multValue = (value / (numerals.roman_to_arabic(roman)))
                checkGobble(multKey, multValue)
            else:
                answer = gobble[item] * numerals.roman_to_arabic(roman)
                return '{0}is {1} Credits'.format(' '.join(keyWords).strip('?'), int(answer))

    answer = numerals.roman_to_arabic(roman)
    return '{0}is {1} Credits'.format(' '.join(keyWords).strip('?'), int(answer))

def checkGobble(keyWord, keyValue, dict=gobble):
    if keyValue in dict.values() or keyWord in dict:
        overwrite = input('Keyword already exists. Do you wish to overwrite? y/n: ')
        if overwrite == 'y':
            writeGobble(keyWord, keyValue)
        elif overwrite != 'n':
            checkGobble(keyWord, keyValue)
    else:
        writeGobble(keyWord, keyValue)

def writeGobble(keyWord, keyValue):
    gobble[keyWord] = keyValue
    fileObj = open('gobble.py', 'w')
    fileObj.write('gobble = ' + pprint.pformat(gobble) + '\n')
    fileObj.close()
    print('Added to dictionary')

if __name__ == "__main__":
    while True:
        inputString = input('Please input here: ')
        if inputString == 'exit':
            break
        else:
            try:
                if not isQuestion(inputString):
                    extractInfo(inputString)
                else:
                    print(extractInfo(inputString, 'calculate'))
            except:
                print('I have no idea what you are talking about')