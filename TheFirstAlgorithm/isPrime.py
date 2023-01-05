import math
from sympy import sieve
from sympy import isprime

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
print(is_prime(11))

print([i for i in sieve.primerange(1,50)])
print(isprime(101))

