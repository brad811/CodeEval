import sys

def primes_sieve(limit):
	a = [True] * limit
	a[0] = a[1] = False

	for (i, isprime) in enumerate(a):
		if isprime:
			yield i
			for n in xrange(i*i, limit, i):
				a[n] = False

test_cases = [i.strip() for i in open(sys.argv[1]).readlines()]
test_cases = map(int, test_cases)

a = list(primes_sieve(max(test_cases)))

for test in test_cases:
	print str([elem for elem in a if elem < test]).replace(' ','')[1:-1]
