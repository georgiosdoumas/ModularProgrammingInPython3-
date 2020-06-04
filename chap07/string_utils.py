import re

def extract_numbers(s):
    pattern = r'[+-]?\d+(?:\.\d+)?'
##    numbers = []
##    for match in re.finditer(pattern, s):
##        number = s[match.start():match.end()]
##        numbers.append(number)
##    return numbers    ## these lines are mentioned in the book
## but we can use list comprehension and do it in one line : 
    return [s[match.start():match.end()] for match in re.finditer(pattern, s)]

