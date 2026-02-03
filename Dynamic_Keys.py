from tables import tabla_ascii
tabla_ascii_inv = {}
for c in tabla_ascii:
    tabla_ascii_inv[tabla_ascii[c]] = c


def generar_llave_dinamica(texto, tabla_ascii, tabla_ascii_inv):
    llave = ""

    for i in range(len(texto)):
        caracter = texto[i]
        ascii_original = tabla_ascii[caracter]

        ascii_nuevo = ascii_original + i

        while ascii_nuevo > 126:
            ascii_nuevo -= 95

        llave += tabla_ascii_inv[ascii_nuevo]

    return llave


texto_base = "Hola123"
llave = generar_llave_dinamica(texto_base, tabla_ascii, tabla_ascii_inv)

print("Texto base:", texto_base)
print("Llave dinámica:", llave)
