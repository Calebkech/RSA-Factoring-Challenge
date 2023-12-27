#!/usr/bin/python3
import sys
import math

def smallest_prime(n):
    if n % 2 == 0:
        return 2
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return i
    return n

def factorize(n):
    p = smallest_prime(n)
    return p, n // p

def main():
    with open(sys.argv[1], 'r') as file:
        for line in file:
            n = int(line)
            p, q = factorize(n)
            print(f"{n}={p}*{q}")

if __name__ == "__main__":
    main()