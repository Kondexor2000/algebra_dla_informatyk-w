from sympy import symbols, Poly, div
from sympy.polys.domains import GF

x = symbols('x')

# Definiujemy wielomiany
f = Poly(x**3 + 2*x**2 + 4*x + 3, domain=GF(7))
g = Poly(3*x**2 + 2, domain=GF(7))

# Wykonujemy dzielenie
quotient, remainder = div(f, g, domain=GF(7))

# Wypisujemy wynik
print(f'Wynik dzielenia: {quotient} reszta: {remainder}')