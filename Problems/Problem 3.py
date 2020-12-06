def count_primes(num):
    primes = [2]
    highest = 0
    x = 3
    if num < 2:
        return 0
    while x <= num/2:
        for y in primes:  # use the primes list!
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            if num%x==0:
                num = num/x
                highest = num
            x += 2
    return highest
print(count_primes(600851475143))
