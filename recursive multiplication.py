def multi(n):
	if n == 0:
		return 1
	else:
		return n*multi(n-1)