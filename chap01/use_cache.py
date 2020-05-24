#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Variation of the book program, to see events of the cache actually being utilized 
"""
import random
import string
import cache  # we can do this, because cache.py is in the same folder as current use_cache.py

def random_string(length):
    s = ''
    for i in range(length):
        s = s + random.choice(string.ascii_lowercase)
    return s

cache.init()
for n in range(200):
    # we assume k,v pairs of the form 'xz':'abcde' , so we create them ramndomly, and the keys have a chance to be repeated
    while True:
        key = random_string(2)  
        if cache.contains(key):
            print("----There was a cache hit!")
            continue
        else:   # there was a chace miss, but I do not print anything to keep my output clearer
            break
    value = random_string(10)
    cache.set(key, value)
    print("After {} iterations, cache has {} entries".format(n+1, cache.size()))
