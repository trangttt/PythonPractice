import sys

def find_logo(array):
    word_list = open('words').read().split('\n')
    for i in range(len(arr)):
        line = ''.join(arr[i])
        words = line.split(' ')
        for w in words:
            if len(w) >= 2:
                if w.lower() in word_list: print(w)
                elif w[::-1].lower() in word_list: print(w[::-1])


    for i in range(len(arr[0])):
        line = ''.join([arr[j][i] for j in range(len(arr))])
        words = line.split(' ')
        for w in words:
            if len(w) >= 2:
                if w.lower() in word_list: print(w)
                elif w[::-1].lower() in word_list: print(w[::-1])

if __name__ == "__main__":
    file = open(sys.argv[1])
    no = int(file.readline().rstrip('\n'))
    arr = [ [] for i in range(no)]
    for i in range(no):
        arr[i] = [ c for c in file.readline().rstrip('\n')]
    length = max( len(arr[i]) for i in range(no))
    for i in range(no):
        if len(arr[i]) != length:
            arr[i] = arr[i] + [' '] * (length - len(arr[i]))
    for i in range(no):
        print(' '.join(arr[i]))
    find_logo(arr)
