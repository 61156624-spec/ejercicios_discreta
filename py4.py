# permutacion
# Programa: combinación C(n, k)
n = int(input("Ingresa n (total de elementos): "))
k = int(input("Ingresa k (elementos que eliges): "))

if k < 0:
    print("k debe estar entre 0 y n.")
else:
    
    

    vr = n**k

    print("vr(", n, ",", k, ") =", vr)