# Variables global
ABC = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


# clave y el texto tienen que tener el mismo tamaño
def igualdad(texto: str, clave: str) -> str:
    """Realizamos que tenga el mismo tamaño la clave y
    el texto"""
    new_clave = ""
    index = 0
    for char in texto:
        if char in ABC:
            new_clave += clave[index % len(clave)]
            index += 1
        else:
            new_clave += char

    return new_clave


# ciframos el texto
def cifrado_vigenere(texto: str, clave: str) -> str:
    cifrado = ""
    if len(clave) <= len(texto):
        clave = igualdad(texto, clave)

    else:
        return "No cumple la condición de cifrado"

    for c, m in zip(clave, texto):
        if m in ABC:
            desplazamiento = (ABC.index(m) + ABC.index(c)) % len(ABC)
            cifrado += ABC[desplazamiento]
        else:
            cifrado += m

    return cifrado


# desciframos el cifrado de vigenere
def descifrado_vigenere(texto_cifrado, clave):
    descifrado = ""
    if len(clave) <= len(texto_cifrado):
        clave = igualdad(texto_cifrado, clave)

    else:
        return "No podemos descifrar la frase, ocurrio algo indeseado"

    for c, m in zip(clave, texto_cifrado):
        if m in ABC:
            desplazamiento = (ABC.index(m) - ABC.index(c)) % len(ABC)
            descifrado += ABC[desplazamiento]
        else:
            descifrado += m

    return descifrado


def main():
    while True:
        texto = input("Ingrese un texto o frase: ").upper()
        if texto:
            break

    while True:
        clave = input("Ingrese clave: ").upper()
        if clave:
            break

    cifrado_vg = cifrado_vigenere(texto, clave)
    print("=" * 40)
    print(f"{'TEXTO : '.ljust(15)}{texto}")
    print(f"{'CIFRADO: '.ljust(15)}{cifrado_vg}")
    print("=" * 40)
    print("\n")
    while True:
        while True:
            op = input("Desea descifrar el texto o frase? (s/n) ").lower()
            if op:
                break
        if op == "s" or op == "si":
            while True:
                clave_descifrar = input("Ingrese la clave para descifrar: ").upper()
                if clave_descifrar == clave:
                    descifrar_vg = descifrado_vigenere(cifrado_vg, clave_descifrar)
                    print("\n")
                    print("=" * 40)
                    print(f"{'TEXTO CIFRADO: '.ljust(17)} {cifrado_vg}")
                    print(f"{'TEXTO DESCIFRADO: '.ljust(17)} {descifrar_vg}")
                    print("=" * 40)
                    break
                else:
                    print("Esa clave no es válida para poder descifrar el texto")
            break
        elif op == "n" or op == "no":
            print("\nOkay, hasta luego")
            break
        else:
            print("\tUps. Hubo un error, ingrese si o no. Por favor")


if __name__ == "__main__":
    main()
