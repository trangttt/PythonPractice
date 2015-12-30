import sys

def game_of_threes(n):
    if n==1:
        print(1)
    elif n % 3 == 0:
        print(n, 0)
        game_of_threes(int(n/3))
    elif n%3 == 1:
        print(n, -1)
        game_of_threes(int((n-1)/3))
    elif n%3 == 2:
        print(n, 1)
        game_of_threes(int((n+1)/3))

if __name__ == "__main__":
    game_of_threes(int(sys.argv[1]))
