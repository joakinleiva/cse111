import tkinter as tk

def say_hello():
    name = entry.get()
    label_output.config(text=f"¡Hola, {name}!")

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo con Tkinter")

# Crear widgets
label = tk.Label(root, text="Escribe tu nombre:")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Saludar", command=say_hello)
button.pack(pady=5)

label_output = tk.Label(root, text="")
label_output.pack(pady=5)

# Iniciar la aplicación
root.mainloop()
