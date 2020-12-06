def count_primes():
    primes = [2]
    x = 3
    while len(primes)<10001:
        for y in primes:  # use the primes list!
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    return max(primes)
print(count_primes())
