def generar_llave_dinamica_ascii(semilla, longitud):
    llave = []
    k = ord(semilla) - 32 

    for i in range(longitud):
        k = (k + i) % 95
        llave.append(k)

    return llave


def cifrar_ascii_llave_dinamica(mensaje, semilla):
    cipher = ""
    llave_dinamica = generar_llave_dinamica_ascii(semilla, len(mensaje))

    for i in range(len(mensaje)):
        ascii_m = ord(mensaje[i]) - 32
        ascii_k = llave_dinamica[i]

        ascii_c = (ascii_m + ascii_k) % 95
        cipher += chr(ascii_c + 32)

    return cipher


# Programa principal
mensaje = "HOLA MUNDO"
semilla = "K"

cipher = cifrar_ascii_llave_dinamica(mensaje, semilla)

print("Mensaje original:", mensaje)
print("Semilla inicial:", semilla)
print("Cipher ASCII:   ", cipher)
