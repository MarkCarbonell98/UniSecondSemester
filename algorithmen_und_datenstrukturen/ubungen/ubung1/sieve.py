def sieve(num):
        limit, primes = num + 1, {}
        for i in range(2, limit): primes[i] = True

        for i in primes:
                factors = range(2*i, limit, i) # start, stop, step
        for f in factors[1:]:
                primes[f] = False
        return [i for i in primes if primes[i]==True]


#losung von Robert

from math import sqrt
def sieve2(n):
        prime = [True] * n
        prime[0] = prime[1] = False
        for i in range(2, int(sqrt(n))):
                for k in range(2 * i, n,i):
                        prime[k] = False
        primes = []
        for k in range(2,n):
                if prime[k]:
                        primes.append(k)
        return primes

print(sieve(20))
print(sieve2(20))
