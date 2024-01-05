# Definicja operacji ⊕
def circle_plus(a, b):
    return a + b - 33

# Sprawdzanie równości dla kilku wartości a i b
for a in range(-10, 10):
    for b in range(-10, 10):
        if a + b != circle_plus(a, b):
            print(f"Dla a={a} i b={b}, a + b nie jest równe a ⊕ b.")
            break
    else:
        continue
    break
else:
    print("Dla wszystkich sprawdzonych wartości a i b, a + b jest równe a ⊕ b.")