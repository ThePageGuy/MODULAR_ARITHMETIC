def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Given primes
p = 26513
q = 32321

# Calculate gcd, u, and v
gcd, u, v = extended_gcd(p, q)

print(f"gcd({p}, {q}) = {gcd}")
print(f"u = {u}, v = {v}")

# Print the lower of u and v
print(f"The lower of u and v is: {min(u, v)}")
