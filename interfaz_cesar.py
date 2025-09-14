import tkinter as tk
from tkinter import ttk


def cesar(texto: str, modo: str = "cifrar") -> str:
    """
    Cifra o descifra un texto usando una variante del cifrado César
    """
    resultado = []

    for indice, caracter in enumerate(texto, start=1):
        # Procesar letras minúsculas
        if "a" <= caracter <= "z":
            base_ord = ord("a")
        # Procesar letras mayúsculas
        elif "A" <= caracter <= "Z":
            base_ord = ord("A")
        else:
            # Para cualquier otro carácter, no se modifica
            resultado.append(caracter)
            continue

        desplazamiento = indice if modo == "cifrar" else -indice
        pos_original = ord(caracter) - base_ord
        pos_nueva = (pos_original + desplazamiento) % 26
        resultado.append(chr(base_ord + pos_nueva))

    return "".join(resultado)


def on_cifrar():
    """botón Cifrar"""
    texto_entrada = entrada.get()
    texto_salida = cesar(texto_entrada, modo="cifrar")
    salida.set(texto_salida)


def on_descifrar():
    """botón Descifrar"""
    texto_entrada = entrada.get()
    texto_salida = cesar(texto_entrada, modo="descifrar")
    salida.set(texto_salida)


#  Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Cifrado César Variable")
ventana.geometry("450x220")
ventana.resizable(False, False)

# Estilos
style = ttk.Style(ventana)
style.configure("TLabel", font=("Segoe UI", 11))
style.configure("TButton", font=("Segoe UI", 11))
style.configure("TEntry", font=("Segoe UI", 11))

marco = ttk.Frame(ventana, padding=15)
marco.pack(expand=True, fill="both")

# Etiqueta y entrada de texto
ttk.Label(marco, text="Texto:").grid(row=0, column=0, sticky="w", pady=5)
entrada = ttk.Entry(marco, width=40)
entrada.grid(row=0, column=1, columnspan=2, sticky="we", padx=5, pady=5)

# Botones
btn_cifrar = ttk.Button(marco, text="Cifrar", command=on_cifrar)
btn_descifrar = ttk.Button(marco, text="Descifrar", command=on_descifrar)
btn_cifrar.grid(row=1, column=1, sticky="e", padx=5, pady=10)
btn_descifrar.grid(row=1, column=2, sticky="w", padx=5, pady=10)

# Resultado
salida = tk.StringVar()
ttk.Label(marco, text="Resultado:").grid(row=2, column=0, sticky="nw", pady=5)
ttk.Label(marco, textvariable=salida, wraplength=400, justify="left").grid(
    row=2, column=1, columnspan=2, sticky="w", pady=5
)

# Ajuste de columnas para que crezcan bien
marco.columnconfigure(1, weight=1)
marco.columnconfigure(2, weight=1)

ventana.mainloop()
