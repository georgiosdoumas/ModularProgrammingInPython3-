import datetime
MAX_CACHE_SIZE = 20

def init():
    global _cache
    _cache = {} # Maps key to (datetime, value) tuple.
    
def set(key, value):
    global _cache
    if key not in _cache and len(_cache) >= MAX_CACHE_SIZE:
        _remove_oldest_entry()
    _cache[key] = [datetime.datetime.now(), value]  # so the _cache[key][0] is the access-time, and _cache[key][1] is the entry's value
    
def get(key):
    global _cache
    if key in _cache:
        print("    We got cache hit!")
        _cache[key][0] = datetime.datetime.now()  # update the access-time of this value
        return _cache[key][1]                     # and return it as result
    else:
        print("    We got cache miss.")
        return None

def contains(key):
    global _cache
    return key in _cache

def size():
    global _cache
    return len(_cache)

def _remove_oldest_entry():  # private function, should be required to access it from outside the module
    global _cache
    oldest = None  # if the _cache dictionary is not empty, it will get some value in the following for loop
    for key in _cache.keys():
        if oldest == None:
            oldest = key
        elif _cache[key][0] < _cache[oldest][0]:
            oldest = key
    if oldest != None:    # then the dictionary _cache was not empty so we have an entry to remove
        print(" Removing oldest entrie:", _cache[oldest])
        del _cache[oldest]
