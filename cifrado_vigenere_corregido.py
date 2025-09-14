ABC = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


def expandir_clave(texto: str, clave: str) -> str:
    nueva_clave = []
    j = 0  # índice para recorrer la clave original
    for char in texto:
        if char.upper() in ABC:
            # tomamos la siguiente letra de la clave (circularmente)
            nueva_clave.append(clave[j % len(clave)])
            j += 1
        else:
            # dejamos espacios, puntuación, números, etc., sin clave
            nueva_clave.append(char)
    return "".join(nueva_clave)


def cifrar_vigenere(texto: str, clave: str) -> str:
    texto = texto.upper()
    clave = clave.upper()
    full_key = expandir_clave(texto, clave)
    resultado = []

    for t_char, k_char in zip(texto, full_key):
        if t_char in ABC:
            # ciframos solo si el caracter está en el alfabeto
            idx = (ABC.index(t_char) + ABC.index(k_char)) % len(ABC)
            resultado.append(ABC[idx])
        else:
            resultado.append(t_char)

    return "".join(resultado)


def descifrar_vigenere(texto_cifrado: str, clave: str) -> str:
    texto_cifrado = texto_cifrado.upper()
    clave = clave.upper()
    full_key = expandir_clave(texto_cifrado, clave)
    resultado = []

    for c_char, k_char in zip(texto_cifrado, full_key):
        if c_char in ABC:
            # desciframos solo si el caracter está en el alfabeto
            idx = (ABC.index(c_char) - ABC.index(k_char)) % len(ABC)
            resultado.append(ABC[idx])
        else:
            resultado.append(c_char)

    return "".join(resultado)


def main():
    texto = input("Ingrese texto: ")
    clave = input("Ingrese clave: ")

    cifrado = cifrar_vigenere(texto, clave)
    print("\n" + "-" * 40)
    print(" TEXTO CIFRADO ".center(40, "-"))
    print(cifrado)
    print("-" * 40)

    respuesta = input("\n¿Desea descifrar este texto? (s/n): ").strip().lower()
    if respuesta in ("s", "si"):
        descifrado = descifrar_vigenere(cifrado, clave)
        print("\n" + "-" * 40)
        print(" TEXTO DESCIFRADO ".center(40, "-"))
        print(descifrado)
        print("-" * 40)
    else:
        print("\n ¡Hasta luego!\n")


if __name__ == "__main__":
    main()
