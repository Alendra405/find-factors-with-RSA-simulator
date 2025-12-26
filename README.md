# Classical RSA Factorization for Small Numbers 🔓

This project implements a **classical algorithm** to factor small composite numbers (N < 100) used in RSA encryption. It demonstrates how weak RSA keys can be broken by finding the order of a random base and using the Euclidean algorithm.

### How It Works?
1. User inputs N (the RSA modulus) and a random number a < N.
2. The program finds the order r (smallest power where a^r ≡ 1 mod N).
3. Computes gcd(a^{r/2} ± 1, N) to find the prime factors p and q.

This is a simplified version of the mathematical attack on RSA when N is small or poorly chosen.

### Features
- Works for very small N (e.g., N = 15 = 3 × 5, N = 21 = 3 × 7).
- Interactive input via console.
- Educational demonstration of RSA vulnerability for weak keys.

### Usage
```bash
python main.py
