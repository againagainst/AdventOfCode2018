"""
Part 1:
abcdef contains no letters that appear exactly two or three times.
bababc contains two a and three b, so it counts for both.
abbcde contains two b, but no letter appears exactly three times.
abcccd contains three c, but no letter appears exactly two times.
aabcdd contains two a and two d, but it only counts once.
abcdee contains two e.
ababab contains three a and three b, but it only counts once.

Of these box IDs, four of them contain a letter which appears exactly 
twice, and three of them contain a letter which appears exactly three 
imes. Multiplying these together produces a checksum of 4 * 3 = 12.

What is the checksum for your list of box IDs?

------
Part 2:
For example, given the following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
The IDs abcde and axcye are close, but they differ by two characters (the 
second and fourth). However, the IDs fghij and fguij differ by exactly one
character, the third (h and u). Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example
above, this is found by removing the differing character from either ID, 
producing fgij.)
"""
from collections import defaultdict
from functools import reduce


def group_letters(txt):
    counter = defaultdict(int)
    for c in txt:
        counter[c] += 1
    grouper = defaultdict(int)
    for v in counter.values():
        grouper[v] += 1
    result = dict(grouper)
    result.pop(1, None)
    return result

def read_data(filename):
    with open(filename, 'r') as fp:
        return fp.read().split('\n')

def checksum(data):
    checksum = defaultdict(int)
    for txt in data:
        g = group_letters(txt)
        for k in g.keys():
            checksum[k] += 1
    return reduce(lambda x, y: x*y, checksum.values())

# part two
def distance(first, second):
    result = 0
    for n in range(len(first)):
        if first[n] != second[n]:
            result += 1
    return result

def find_closest(data):
    data = sorted(data)
    for line in data:
        for other_line in data:
            if line == other_line:
                continue
            if distance(line, other_line) == 1:
                return line, other_line

def substract(first, second):
    result = []
    for n in range(len(first)):
        if first[n] == second[n]:
            result.append(first[n])
    return ''.join(result)

if __name__ == "__main__":
    data = read_data('data.txt')
    print(substract(*find_closest(data)))