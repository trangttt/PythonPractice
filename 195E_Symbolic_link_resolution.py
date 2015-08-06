import sys

file = open(sys.argv[1])

no_l = int(file.readline())

rules = []
for i in range(no_l):
    link, dest = file.readline().rstrip(' /\n').split(":")
    rules.append((link, dest))

quest = file.readline().strip()

tested = no_l
while tested > 0:
    for i in range(no_l):
        if quest.startswith(rules[i][0]):
            print(rules[i])
            print(quest)
            quest = quest.replace(rules[i][0], rules[i][1])
            print(quest)
            print()
            tested = no_l
        else:
            tested -= 1

print(quest)
