from collections import Counter
import math

class Solution:
    def maxKPower(self, n: int, k: int) -> int:
        
        # Prime factorization of k
        def prime_factors(x):
            factors = Counter()
            d = 2
            while d * d <= x:
                while x % d == 0:
                    factors[d] += 1
                    x //= d
                d += 1
            if x > 1:
                factors[x] += 1
            return factors
        
        # Legendre's formula for a prime p in n!
        def legendre(n, p):
            count = 0
            power = p
            while power <= n:
                count += n // power
                power *= p
            return count

        factors = prime_factors(k)
        min_power = float('inf')
        
        for prime, exp in factors.items():
            total = legendre(n, prime)
            min_power = min(min_power, total // exp)

        return min_power
