def primes_sieve1(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]

primes = primes_sieve1(10**6)
primes_set = set(primes)

longest_range = -1
longest_val = None
for p1 in range(len(primes)):
    s = 0
    for p2 in range(p1, len(primes)):
        s += primes[p2]
        if s > 10**6:
            break

        if s in primes_set and p2 - p1 > longest_range:
            longest_val = (f"From {primes[p1]} to {primes[p2]}: {s}")
            longest_range = p2 - p1

print(longest_val, longest_range)

