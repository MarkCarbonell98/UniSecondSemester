def sieve(num):
    limit, primes = num + 1, {}
    for i in range(2, limit): primes[i] = True
    
    for i in primes:
        factors = range(i, limit, i) # start, stop, step
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]
