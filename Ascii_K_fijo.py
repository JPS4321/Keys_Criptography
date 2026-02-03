from tables import tabla_ascii

# Tabla inversa
tabla_ascii_inv = {}
for c in tabla_ascii:
    tabla_ascii_inv[tabla_ascii[c]] = c

# Alfabeto válido ordenado
alfabeto = sorted(tabla_ascii.keys(), key=lambda x: tabla_ascii[x])
N = len(alfabeto)


def cifrar_ascii(mensaje, llave):
    cipher = ""
    len_llave = len(llave)

    for i in range(len(mensaje)):
        char_m = mensaje[i]
        char_k = llave[i % len_llave]

        # índices dentro del alfabeto
        idx_m = alfabeto.index(char_m)
        idx_k = alfabeto.index(char_k)

        # cifrado modular
        idx_c = (idx_m + idx_k) % N

        cipher += alfabeto[idx_c]

    return cipher


# Programa principal
mensaje = "HOLA MUNDO"
llave_k = "KEY"

cipher = cifrar_ascii(mensaje, llave_k)

print("Mensaje original:", mensaje)
print("Llave fija k:    ", llave_k)
print("Cipher ASCII:    ", cipher)
