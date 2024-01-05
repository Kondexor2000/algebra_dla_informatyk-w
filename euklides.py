def rozwiązanie(a, b, c):
    def rozszerzony_euklides(a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = rozszerzony_euklides(b % a, a)
            return gcd, y - (b // a) * x, x

    gcd, x, y = rozszerzony_euklides(a, b)

    if c % gcd != 0:
        return None
    else:
        x *= c // gcd
        y *= c // gcd
        return x, y

x, y = rozwiązanie(58, 31, 7)
print(f"x = {x}, y = {y}")