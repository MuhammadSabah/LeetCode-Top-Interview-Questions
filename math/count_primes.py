class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True] * (n)

        for i in range(2, n):
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = False

        return len([i for i in range(2, n) if primes[i]])