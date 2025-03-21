import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "A tarefa não pode estar vazia!")

def remove_task():
    try:
        selected_task = task_list.curselection()[0]
        task_list.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para remover!")

def clear_tasks():
    task_list.delete(0, tk.END)

# Criando a janela principal
root = tk.Tk()
root.title("Lista de Tarefas")
root.geometry("400x400")

# Criando widgets
task_entry = tk.Entry(root, width=40)
add_button = tk.Button(root, text="Adicionar", command=add_task)
remove_button = tk.Button(root, text="Remover", command=remove_task)
clear_button = tk.Button(root, text="Limpar Tudo", command=clear_tasks)
task_list = tk.Listbox(root, width=50, height=15)

# Posicionando widgets
task_entry.pack(pady=10)
add_button.pack()
remove_button.pack()
clear_button.pack()
task_list.pack(pady=10)

# Iniciando loop principal
root.mainloop()
