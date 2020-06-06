import string
import random

def random_name(min_chars, max_chars):
    """ Produces a string of ascii characters, of length equal to a random length
        chosen between the values min_chars and max_chars
        Input :
          min_chars: Integer, the shortest possible length of the produced random word
          max_chars: Integer, the longest possible length of the produced random word
        Returns: a string """
    assert min_chars < max_chars
##    chars = []
##    for i in range(random.randrange(min_chars, max_chars)):
##        chars.append(random.choice(string.ascii_letters))
##  The book has the above 3 lines on page 198, but we can do better :    
    chars = [random.choice(string.ascii_letters) for i in range(random.randrange(min_chars, max_chars))]
    return "".join(chars)


def run(number_of_words_to_create, low, high):
    for i in range(number_of_words_to_create):
        print(random_name(low, high)) 
