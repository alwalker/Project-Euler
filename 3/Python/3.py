def getPrimes(numPrimes, prev):
	primes = prev
	max = prev[-1]
	while(len(primes) < numPrimes):
		for i in range(prev[-1] + 1, max):
			isPrime = True
			for j in range(2, i - 1):
				if i % j == 0:
					isPrime = False
					break
			if isPrime:
				primes.append(i)
		max = max + 1
	return primes

def getPrimeFactors(num):
	primes = getPrimes(100, [2])
	factors = []
	dividePrime(factors, primes, num)
	return factors

def dividePrime(factors, primes, num):
	if num == 1 or num in primes:
		factors.append(num)
		return
	for prime in primes:
		if num % prime == 0:
			if prime not in factors:
				factors.append(prime)
			dividePrime(factors, primes, num/prime)
			return
	if primes[-1] < num:
		primes = getPrimes(len(primes) + 1, primes)
		dividePrime(factors, primes, num)

factors = getPrimeFactors(600851475143)
print "Largest prime factor:\t" + str(factors[-1])