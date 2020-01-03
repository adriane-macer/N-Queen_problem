# created by Adrian Evangelista

from itertools import permutations

patterns = {}


def is_q_num(positions,n):
    # checks diagonals
    for x in range(n):
        # from top row left to right back slash
        # [?__..n]
        # [_?_..n]
        # [__?..n]
        # ...
        # [___..?]
        if sum(int(patterns.get(positions[y-x])[y]) for y in range(x,n)) > 1:
            return False
        # from top row to rigth forward slash
        # [___..?]
        # ...
        # [__?..n]
        # [_?_..n]
        #[?__..n]
        if sum(int(patterns.get(positions[y])[x-y]) for y in range(len(positions[:x])+1)) > 1:
            return False
          
    for y in range(1,n):
        # right side forward slash check
        # [_..__n]
        # [_..__?]
        # [_.._?n]
        # [_..?_n]
        # ...
        # [?..__n]
        # [_..__n]
        if sum(int(patterns.get(positions[y+x])[n-x-1]) for x in range(len(positions[y:]))) >1:
            return False
        # left side backslash
        # [__.._n]
        # [?_.._n]
        # [_?.._n]
        # ...
        # [__..?n]
        if sum(int(patterns.get(positions[y+x])[x]) for x in range(len(positions[y:]))) > 1:
            return False
            
    return True

def unique_permutations(iterable, r=None):
    previous = tuple()
    for p in permutations(sorted(iterable), r):
        if p > previous:
            previous = p
            yield p   

       
# starts here
print("input size :")
size = int(input())
# genrate ordered pattern as keys for patterns (e.g. [1,2,3,4] for size 4 board)
ordered_pattern = [x for x in range(0,size)]
# make a dictionary for all patterns
# ordered_pattern elements use as keys for the patterns dictionary
# thus the size of the dictionary equal to the size of the side of the board
for i, pattern in enumerate(ordered_pattern):
    patterns[i]='0'*i + '1'.ljust(size-i,'0')

num_of_possibilities=0
# enumerate all the possible combinations
# then check if n-queens 
# prints if n-queens
for p in unique_permutations(ordered_pattern):
    
    if is_q_num(p,size):
        # prints the n-quuens pattern
        # divider
        print("*********************")
        num_of_possibilities += 1
        print('*****',num_of_possibilities,'*****')
        for row in p:
            print(patterns.get(row))
            
            
print(num_of_possibilities, "number of possible patterns")
