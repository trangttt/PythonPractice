lines = open("221I_input.txt").read().splitlines()
canvas = { (x,y):c for x,line in enumerate(lines) for y,c in enumerate(line) if c != ' '}

dirs = [(1,0), (0,1), (-1,0), (0,-1)]


result = []
print(canvas)

current = (0,0)
word = [canvas.get(current,'*')]
del canvas[current]

while len(canvas) > 0:
        for dir in dirs:
            next = tuple( [t1+t2 for t1,t2 in zip(current,dir)])
            if next in canvas :
                while next in canvas :
                    current = next
                    word.append(canvas.get(current))
                    del canvas[current]
                    next = tuple([t1+t2 for t1,t2 in zip(current,dir)])
                result.append("".join(word))
                word = [word[-1]]
            else :
                continue


print(" ".join(result))
