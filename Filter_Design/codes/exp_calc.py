from sympy import symbols, simplify

# Define symbolic variable s
s = symbols('s')

# Constants
omega0_val = 0.49167
B_val = 0.0977

# Define s_L in terms of s, omega0, and B
s_L = (s**2 + omega0_val**2) / (B_val * s)

# Given roots
s5 = -0.1621 -1.0033j
s6 = -0.3913 -0.4156j
s7 = -0.3913 + 0.4156j
s8 = -0.1621 + 1.0033j

# Define the given polynomial expression
polynomial_expr = 1.0771 / ((s_L - s5) * (s_L - s6) * (s_L - s7) * (s_L - s8))

# Simplify the expression
simplified_expr = simplify(polynomial_expr)

# Print the simplified expression
print("Simplified Polynomial in terms of s:")
print(simplified_expr)
