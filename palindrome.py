import sys


def other_solution(n):
	ret = True
	l = len(n)
	for i in range(l):
		if n[i] != n[l-i-1]:
			ret = False
			break
	return ret

def main(n):
	reversed = n[::-1]
	if (reversed == n) :
		print 'Your number is palindrome'
	else :
		print 'Your number is not palindrome'
	print other_solution(n)

def usage(func):
	USAGE = '''
			%s <number>
			usage: check if <number> is palindrome
			'''
	print USAGE % func

if __name__ == "__main__" :
	if len(sys.argv) == 2:
		main(sys.argv[1])	
	else :
		usage(sys.argv[0])	
