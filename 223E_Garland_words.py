input = ["programmer", "ceramic", "onion", "alfalfa"]


def garland(str):
    for i in range(len(str)-1, 0, -1):
        if str[:i] == str[len(str)-i:]:
            return i


for entry in input:
    print(entry, garland(entry))
