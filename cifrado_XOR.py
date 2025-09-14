def cifrado_xor(texto: str, clave: str) -> str:
    new_cifrado = ""
    for i in range(len(texto)):
        # la clave y el texto tienen que tener el mismo tamaño
        char_texto = texto[i]
        char_clave = clave[i % len(clave)]

        # usamos el operador ^, esto opera a nivel de bits (0, 1)
        cifrado = ord(char_texto) ^ ord(char_clave)
        new_cifrado += chr(cifrado)

    return new_cifrado


def main():
    while True:
        texto = input("Ingrese una frase o texto: ")
        if texto:
            break

    while True:
        clave = input("Ingrese la clave: ")
        if clave:
            break

    print("-" * 40)
    print("Cifrado XOR (cifrado a nivel bits)".center(40))
    print("-" * 40)

    # llamaos a la funcion cifrado oxr
    xor_cifrado = cifrado_xor(texto, clave)
    print(
        f"\n\t{'Texto:'.ljust(15)} {texto}\n\t{'Texto cifrado:'.ljust(15)} {xor_cifrado}\n"
    )

    # para descifrar usamos la misma clave dos veces
    xor_descifrado = cifrado_xor(xor_cifrado, clave)
    print(
        f"\n\t{'Texto cifrado:'.ljust(20)} {xor_cifrado}\n\t{'Texto descifrado:'.ljust(20)} {xor_descifrado}\n"
    )


if __name__ == "__main__":
    main()
