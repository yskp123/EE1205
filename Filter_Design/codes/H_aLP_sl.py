import sympy as sp

# Define the variable
s = sp.symbols('s')

# Given roots
s5 = -0.1621 -1.0033j
s6 = -0.3913 -0.4156j
s7 = -0.3913 + 0.4156j
s8 = -0.1621 + 1.0033j

# Convert the roots to sympy complex numbers
s5_sp = sp.sympify(s5)
s6_sp = sp.sympify(s6)
s7_sp = sp.sympify(s7)
s8_sp = sp.sympify(s8)

# Define the polynomial
poly = (s - s5_sp) * (s - s6_sp) * (s - s7_sp) * (s - s8_sp)

# Expand the polynomial
expanded_poly = sp.expand(poly)

# Print the expanded polynomial
print(0.3125/(expanded_poly))

