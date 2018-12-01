import pprint

def get_calibration():
    with open('data.txt', 'r') as fp:
        txt = fp.read()
        txt = txt.replace('\n', ' ')
        return eval(txt)

def get_first_reach_twice(ncycles=300):
    current = 0
    freqs = {current}
    for cycle in range(ncycles):
        with open('data.txt', 'r') as fp:
            for line in fp:
                current = eval('{} {}'.format(current, line))
                if current in freqs:
                    return current, "Cycles: {}".format(cycle)
                freqs.add(current)
    return "Cycles: {}".format(cycle)


if __name__ == "__main__":
    print(get_first_reach_twice())
