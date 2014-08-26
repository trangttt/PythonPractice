from collections import defaultdict

data_file = 'windfarm.dat.txt'


def tree():
    return defaultdict(int)

def load_data(fn):
    farm_data = defaultdict(tree)
    with open(fn) as f:
        for line in f:
            tower, day, kwh = line.strip().split()
            farm_data[int(tower)][day] += int(kwh)
    return farm_data


def print_table(data):
    fields = ('Tower', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
    template = '|' + '|{:^10}|' * len(fields)
    print template.format(*fields)
    print template.format(* ['=' * 10] * len(fields))
    for tower in sorted(data.keys()):
        tdata = [ data[tower][day] for day in fields[1:] ]
        print template.format(tower, *tdata)

if __name__ == '__main__' :
    print_table(load_data(data_file))

__author__ = 'dantoccatu'
