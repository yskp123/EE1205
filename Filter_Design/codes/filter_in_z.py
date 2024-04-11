import sympy as sp

# Define symbols
s, z = sp.symbols('s z')

# Given transfer function
Ha_BP_s = s**4/(s**8 + 0.108*s**7 + 0.982*s**6 + 0.079*s**5 + 0.358*s**4 + 0.0192*s**3 + 0.0574*s**2 + 0.0015*s + 0.0034)

# Perform substitution
substitution = ((1 - z**-1) / (1 + z**-1))
substituted_expression = Ha_BP_s.subs(s, substitution)

# Simplify the expression
simplified_expression = sp.simplify(substituted_expression)

# Print the result
print("Expression in z:")
print(simplified_expression)


