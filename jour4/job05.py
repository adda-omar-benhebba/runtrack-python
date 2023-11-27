def remplacer_element(L):
    L[3] = L[2] + L[4]
    return L

L = [1, 2, 3, 4, 5]
print(L[1])
L = remplacer_element(L)
print(L)
print(L[-1])
