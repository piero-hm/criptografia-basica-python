import tkinter as tk
from tkinter import ttk, messagebox

# Importamos las funciones de cifrado desde el archivo corregido
from cifrado_vigenere_corregido import cifrar_vigenere, descifrar_vigenere


def on_procesar(modo: str):
    texto_entrada = entrada_texto.get("1.0", "end-1c").strip()
    clave = entrada_clave.get().strip()

    if not texto_entrada:
        messagebox.showwarning(
            "Entrada vacía", "Por favor, introduce el texto que deseas procesar."
        )
        return
    if not clave:
        messagebox.showwarning("Clave vacía", "El cifrado Vigenère requiere una clave.")
        return

    if modo == "cifrar":
        texto_salida = cifrar_vigenere(texto_entrada, clave)
    else:
        texto_salida = descifrar_vigenere(texto_entrada, clave)

    # Limpiamos el widget de salida y mostramos el nuevo resultado
    salida_texto.config(state="normal")
    salida_texto.delete("1.0", "end")
    salida_texto.insert("1.0", texto_salida)
    salida_texto.config(state="disabled")


#  Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Cifrado Vigenère")
ventana.geometry("500x450")
ventana.resizable(True, True)
ventana.minsize(450, 400)

# Estilos para una apariencia más moderna
style = ttk.Style(ventana)
style.theme_use("clam")  # 'clam', 'alt', 'default', 'classic'
style.configure("TLabel", font=("Segoe UI", 11))
style.configure("TButton", font=("Segoe UI", 11, "bold"))
style.configure("TEntry", font=("Segoe UI", 11))
style.configure("TFrame", background="#f0f0f0")

marco = ttk.Frame(ventana, padding=20)
marco.pack(expand=True, fill="both")

# Etiqueta y entrada para el texto
ttk.Label(marco, text="Texto a procesar:").grid(
    row=0, column=0, columnspan=2, sticky="w", pady=(0, 5)
)
entrada_texto = tk.Text(
    marco,
    width=50,
    height=8,
    font=("Segoe UI", 11),
    wrap="word",
    borderwidth=2,
    relief="groove",
)
entrada_texto.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=5)

# Etiqueta y entrada para la clave
ttk.Label(marco, text="Clave:").grid(row=2, column=0, sticky="w", pady=(10, 5))
entrada_clave = ttk.Entry(marco, width=30)
entrada_clave.grid(row=2, column=1, sticky="we", pady=(10, 5), padx=(5, 0))

# Botones
marco_botones = ttk.Frame(marco)
marco_botones.grid(row=3, column=0, columnspan=2, pady=15)
btn_cifrar = ttk.Button(
    marco_botones, text="Cifrar", command=lambda: on_procesar("cifrar")
)
btn_descifrar = ttk.Button(
    marco_botones, text="Descifrar", command=lambda: on_procesar("descifrar")
)
btn_cifrar.pack(side="left", padx=10)
btn_descifrar.pack(side="left", padx=10)

# Etiqueta y widget de texto para el resultado
ttk.Label(marco, text="Resultado:").grid(
    row=4, column=0, columnspan=2, sticky="w", pady=(10, 5)
)
salida_texto = tk.Text(
    marco,
    width=50,
    height=8,
    font=("Segoe UI", 11),
    wrap="word",
    state="disabled",
    borderwidth=2,
    relief="groove",
)
salida_texto.grid(row=5, column=0, columnspan=2, sticky="nsew", pady=5)

# Configuración de expansión de filas y columnas
marco.rowconfigure(1, weight=1)
marco.rowconfigure(5, weight=1)
marco.columnconfigure(1, weight=1)

ventana.mainloop()
