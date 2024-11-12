import tkinter as tk
from tkinter import messagebox

# Configuración de la ventana principal
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Lista de tareas
tasks = []

# Función para actualizar la lista mostrada
def update_task_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Función para agregar una nueva tarea
def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append(task)
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No puedes agregar una tarea vacía.")

# Función para eliminar la tarea seleccionada
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        del tasks[selected_task_index]
        update_task_list()
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

# Función para marcar una tarea como completada
def mark_task_completed():
    try:
        selected_task_index = listbox.curselection()[0]
        tasks[selected_task_index] += " - Completada"
        update_task_list()
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcar como completada.")

# Entrada para nueva tarea
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# Botones de agregar, eliminar y marcar como completada
add_button = tk.Button(root, text="Agregar Tarea", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Eliminar Tarea", command=delete_task)
delete_button.pack(pady=5)

complete_button = tk.Button(root, text="Marcar como Completada", command=mark_task_completed)
complete_button.pack(pady=5)

# Listbox para mostrar las tareas
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
