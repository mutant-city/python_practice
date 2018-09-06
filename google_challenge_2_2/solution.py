import string
from copy import deepcopy

def answer(n,b):
    return run(n,b)

def run(val, base, tune = 1000):
    list = []
    next = val
    for i in range(0, tune):
        next = getNext(next, base)
        list.append(next)
        r = findSmallestWindowSize(list)
        if r > 0: return r
    return 0

def getNext(val, base):
    length = len(str(val))
    sorted_x = sorted(str(val), reverse=True)
    sorted_y = sorted(str(val))
    x = int(''.join(sorted_x), base) # ascending
    y = int(''.join(sorted_y), base)# descending
    z = int2base(x - y, base).zfill(length)
    return z

# converts from int to a base
def int2base(x, base, type='s'):
    digs = string.digits + string.ascii_letters

    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()
    final = ''.join(digits)
    if(type=='i'): return int(final)
    return final

# finds the smallest repetition size, i.e. the smallest window size thats not composed of any smaller windows
def findSmallestWindowSize(value_list):
    max = 0
    max_i = 0
    for i in range(0, len(value_list)):
        cycle = hasEndCycle(value_list, i)
        if cycle > max: 
            max = cycle
            max_i = i
    return max_i

# returns number of END repetitions of the window or zero if no END repetitions
def hasEndCycle(value_list, window_size):
    if window_size == 0: return 0
    inc = 0
    for j in range(0, len(value_list) - window_size):
        for i in range(j,len(value_list) - window_size, window_size):
            first_val = value_list[i:i+window_size]
            second_val = value_list[i+window_size:i+(window_size*2)]
            if first_val == second_val:
                inc += 1
            else:
                inc = 0 
        if inc > 0: 
            inc += 1
            return inc
    return 0