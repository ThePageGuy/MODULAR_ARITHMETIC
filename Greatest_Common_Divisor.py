def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Test the function with the given example
a = 12
b = 8
print(f"The GCD of {a} and {b} is {gcd(a, b)}")

# Calculate the GCD for the provided numbers
a = 66528
b = 52920
print(f"The GCD of {a} and {b} is {gcd(a, b)}")
