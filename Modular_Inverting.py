# Given values
g = 3
p = 13

# Calculate the inverse using Fermat's Little Theorem
inverse_d = pow(g, p-2, p)

# Print the result
print(f"The inverse of {g} modulo {p} is {inverse_d}")
