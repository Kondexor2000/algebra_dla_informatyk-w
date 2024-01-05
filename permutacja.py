# Twoja permutacja
permutation = {1: 3, 2: 4, 3: 5, 4: 8, 5: 7, 6: 1, 7: 9, 8: 6, 9: 2}

# Obliczanie odwrotności permutacji
def invert(permutation):
    return {v: k for k, v in permutation.items()}

# Rozkładanie permutacji na cykle
def cycles(permutation):
    remaining = set(permutation)
    while remaining:
        start = remaining.pop()
        cycle = [start]
        while True:
            start = permutation[start]
            if start not in remaining:
                break
            remaining.remove(start)
            cycle.append(start)
        yield cycle

# Rozkładanie cyklu na transpozycje
def transpositions(cycle):
    return [(cycle[i - 1], cycle[i]) for i in range(1, len(cycle))]

# Wyświetlanie wyników
print("C^-1:", invert(permutation))
for cycle in cycles(permutation):
    print("Cycle:", cycle)
    print("Transpositions:", transpositions(cycle)) 