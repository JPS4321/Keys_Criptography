# Tabla ASCII (carácter → decimal)
tabla_ascii = {
    ' ':32,
    **{chr(i): i for i in range(33, 127)}
}

# Tabla ASCII inversa (decimal → carácter)
tabla_ascii_inv = {}
for c in tabla_ascii:
    tabla_ascii_inv[tabla_ascii[c]] = c


def cifrar_ascii(mensaje, llave, tabla_ascii, tabla_ascii_inv):
    cipher = ""
    len_llave = len(llave)

    for i in range(len(mensaje)):
        char_m = mensaje[i]
        char_k = llave[i % len_llave]

        ascii_m = tabla_ascii[char_m]
        ascii_k = tabla_ascii[char_k]

        # cifrado ASCII (rango imprimible)
        ascii_c = ((ascii_m + ascii_k - 32) % 95) + 32

        cipher += tabla_ascii_inv[ascii_c]

    return cipher


# Programa principal
mensaje = "HOLA MUNDO"
llave_k = "KEY"

cipher = cifrar_ascii(mensaje, llave_k, tabla_ascii, tabla_ascii_inv)

print("Mensaje original:", mensaje)
print("Llave fija k:    ", llave_k)
print("Cipher ASCII:    ", cipher)
