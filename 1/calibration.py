"""
Task #1
Current frequency  0, change of +1; resulting frequency  1.
Current frequency  1, change of -2; resulting frequency -1.
Current frequency -1, change of +3; resulting frequency  2.
Current frequency  2, change of +1; resulting frequency  3.
In this example, the resulting frequency is 3.

Here are other example situations:

+1, +1, +1 results in  3
+1, +1, -2 results in  0
-1, -2, -3 results in -6
Starting with a frequency of zero, what is the resulting frequency after 
all of the changes in frequency have been applied?

Task #2
You notice that the device repeats the same frequency change list over and over. 
To calibrate the device, you need to find the first frequency it reaches twice.

For example, using the same list of changes above, the device would loop as follows:

Current frequency  0, change of +1; resulting frequency  1.
Current frequency  1, change of -2; resulting frequency -1.
Current frequency -1, change of +3; resulting frequency  2.
Current frequency  2, change of +1; resulting frequency  3.
(At this point, the device continues from the start of the list.)
Current frequency  3, change of +1; resulting frequency  4.
Current frequency  4, change of -2; resulting frequency  2, which has already been seen.

What is the first frequency your device reaches twice?
"""

import itertools

def get_calibration():
    with open('data.txt', 'r') as fp:
        txt = fp.read()
        txt = txt.replace('\n', ' ')
        return eval(txt)

def get_first_reach_twice(ncycles=300):
    current = 0
    freqs = {current}
    with open('data.txt', 'r') as fp:
        data = [int(l) for l in fp]
    data_cycled = itertools.cycle(data)
    for num in data_cycled:
        current = current + num
        if current in freqs:
            return current
        freqs.add(current)


if __name__ == "__main__":
    print(get_calibration())
    print(get_first_reach_twice())
