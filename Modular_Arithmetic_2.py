# Given prime p
p = 17

# Calculate 3^17 mod 17
result1 = pow(3, 17, p)

# Calculate 5^17 mod 17
result2 = pow(5, 17, p)

# Calculate 7^16 mod 17
result3 = pow(7, 16, p)

# Print the results
print(f"3^17 ≡ {result1} mod 17")
print(f"5^17 ≡ {result2} mod 17")
print(f"7^16 ≡ {result3} mod 17")

# Calculate 27324678765465536 mod 65537
p_large = 65537
large_number = 27324678765465536
result4 = large_number % p_large

# Print the result
print(f"27324678765465536 ≡ {result4} mod 65537")
