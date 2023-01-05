#!/usr/bin/env python3
import array

numOfPrimes = 500
primes = [0]*numOfPrimes

num = 7
maxSquare = 2

primes[0] = 2
primes[1] = 3
primes[2] = 5

for b in range(3, len(primes)):
    i = 1
    while i <= maxSquare:
        if num%primes[i]==0:
            num+=2
            if(maxSquare+1)*(maxSquare+1) <= num:
                maxSquare+=1
            i=0
        i+=1
    primes[b] = num
    num+=2
    if(maxSquare+1)*(maxSquare+1) <= num:
        maxSquare+=1

print(primes)