# Definicja pierścienia Z5
Z5 = [0, 1, 2, 3, 4]

# Obliczanie elementów przeciwnych
opposite_elements = {a: -a % 5 for a in Z5}
print("Elementy przeciwne w Z5:", opposite_elements)

# Obliczanie elementów odwrotnych
inverse_elements = {a: next((b for b in Z5 if (a*b) % 5 == 1), 'Brak') for a in Z5}
print("Elementy odwrotne w Z5:", inverse_elements)