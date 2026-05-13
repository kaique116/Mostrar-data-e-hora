# Importa as bibliotecas necessárias
import time
import tkinter as tk
from tkinter import messagebox
import pandas as pd

# Cria a função para mostrar a hora e data atual
def hora_e_data():
    # Cria uma variavel para armazenar a hora e data atual
    hora_atual = time.strftime("%H:%M:%S")
    data_atual = time.strftime("%d/%m/%Y")

    # Exibe a hora e a data atual em uma nova janela
    messagebox.showinfo("Hora e Data", f"Hora: {hora_atual}\nData: {data_atual}")


# Cria a janela principala
janela = tk.Tk()
janela.title("Hora de Data")
janela.geometry("300x200")

#Cria o botão com a função para mostrar a hora e data atual
Botao = tk.Button(janela, text="Mostrar Hora e Data", command=hora_e_data)
Botao.pack(pady=20)

# Cria o loop principal da janela
janela.mainloop()
