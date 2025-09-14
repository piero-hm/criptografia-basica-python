def cifrado_cesar(texto: str) -> str:
    """Ciframos los caracteres respecto a su desplazamiento
    en este contexto, el desplazamiento es su indice de la cadena"""

    new_text = ""
    for index, letra in enumerate(texto, start=1):
        if "a" <= letra <= "z":
            # 1. Convertir la letra a su posición en el abecedario (a=0, b=1, ...)
            posicion = ord(letra) - ord("a")
            # 2. Sumar el índice y usar módulo 26 para el efecto "circular"
            nueva_posicion = (posicion + index) % 26
            # 3. Convertir la nueva posición de vuelta a una letra
            new_text += chr(ord("a") + nueva_posicion)
        elif "A" <= letra <= "Z":
            posicion = ord(letra) - ord("A")
            nueva_posicion = (posicion + index) % 26
            new_text += chr(ord("A") + nueva_posicion)
        else:
            # Si no es una letra, la dejamos como está
            new_text += letra

    return new_text


def descifrado_cesar(new_texto: str) -> str:
    """A partir del cifrado, ahora desciframos la frase o el texto"""

    descifrado = ""
    for index, letra in enumerate(new_texto, start=1):
        if "a" <= letra <= "z":
            # 1. Convertir la letra cifrada a su posición (0-25)
            posicion_cifrada = ord(letra) - ord("a")
            # 2. Restar el índice (la operación inversa) y usar módulo 26
            posicion_original = (posicion_cifrada - index) % 26
            # 3. Convertir la posición original de vuelta a una letra
            descifrado += chr(ord("a") + posicion_original)

        elif "A" <= letra <= "Z":
            posicion_cifrada = ord(letra) - ord("A")
            posicion_original = (posicion_cifrada - index) % 26
            descifrado += chr(ord("A") + posicion_original)

        else:
            # Si no es una letra, la dejamos como está
            descifrado += letra
    return descifrado


def main():
    while True:
        ingresar = input("Desea cifrar una frase? (si/no) ").lower()
        if ingresar == "si" or ingresar == "s":
            while True:
                texto_user = input("Frase: ").strip()
                if texto_user:
                    break

            # Llamamos a la función cifrado cesar
            new_cifrado = cifrado_cesar(texto_user)
            print("-" * 40)
            print("Frase cifrada: ", new_cifrado)
            print("-" * 40)

            # Desiframos el mensaje o la frase:
            frase_descifrado = descifrado_cesar(new_cifrado)
            print("-" * 40)
            print("Frase descifrada: ", frase_descifrado)
            print("-" * 40)

        elif ingresar == "no" or ingresar == "n":
            print("\nGracias por participar. Hasta pronto.")
            break

        else:
            print("\nUps!! Hubo un error, vuelva a ingresar si o no\n")
            continue


if __name__ == "__main__":
    main()
