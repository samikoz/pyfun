# Eratosthenes sieve, 64 bytes
def p(n):return[]if n==1else all(n%q for q in p(n-1))*[n]+p(n-1)


if __name__ == '__main__':
	assert p(1) == []
	assert p(5) == [5, 3, 2]
	assert p(12) == [11, 7, 5, 3, 2]
