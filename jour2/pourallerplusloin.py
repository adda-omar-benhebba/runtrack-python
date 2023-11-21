def est_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True

def type_triangle(a, b, c):
    if a == b == c:
        return "equilatéral"
    elif a == b or b == c or a == c:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "rectangle et isocèle"
        return "isocèle"
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return "rectangle"
    return "quelconque"

a = float(input("Entrez la longueur a : "))
b = float(input("Entrez la longueur b : "))
c = float(input("Entrez la longueur c : "))

if est_triangle(a, b, c):
    print("Ces longueurs peuvent former un triangle", type_triangle(a, b, c))
else:
    print("Ces longueurs ne peuvent pas former un triangle.")
