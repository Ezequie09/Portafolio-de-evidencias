import tkinter as tk
from tkinter import messagebox

# Función para mostrar el texto ingresado
def mostrar_texto():
    texto = entrada.get()
    messagebox.showinfo("Texto ingresado", f"Has escrito: {texto}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Interfaz Gráfica")

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="Escribe algo:")
etiqueta.pack(pady=10)

# Crear un cuadro de entrada
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=10)

# Crear un botón que llama a la función 'mostrar_texto'
boton = tk.Button(ventana, text="Mostrar", command=mostrar_texto)
boton.pack(pady=10)

# Iniciar el bucle principal de la interfaz
ventana.mainloop()
