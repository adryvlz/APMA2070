#%%
import numpy as np

# HW1, problem 1 (Forward Difference)

# Define the function f(x)
def f(x):
    return x**2 + 2*x + 1

# Define the forward difference formula
def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h

# Given values
x = 2
h = 0.01

# Compute the numerical derivative using forward difference
f_prime_approx = forward_difference(f, x, h)

# Display the result
print (f_prime_approx)

# Problem #2 (Center Difference)
def g(x):
    return np.sin(x)

def center_diff(g, x, h):
    return (g(x + h) - 2 * g(x) + g(x - h)) / h**2

# Update values
x = np.pi / 4
h = 0.1

# Compute with central
g_central_approx = center_diff(g, x, h)

print(g_central_approx)

# Problem #3 (Error Analysis in Differentiation)
# We know that the analytical derivate of e^x should be xe^x
# evaluate given the following steps:

# update x
x = 1

h1 = 0.1 
h2 = 0.01
h3 = 0.001

def h(x):
    return np.exp(x)

print(forward_difference(h, x, h1))
print(forward_difference(h, x, h2))
print(forward_difference(h, x, h3))

# as seen, the difference compared to the analytical value of 2.71828182846 becomes closer as we decrease step size.
#%%
# Numerical Integration #

