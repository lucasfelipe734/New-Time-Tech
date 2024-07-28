import tkinter as tk  # Importa o módulo tkinter como tk
import os  # Importa o módulo os

def check_conversion(num_str):
    """
    Função para verificar se é possível converter a string para um número inteiro.
    Retorna True se for possível, False caso contrário.
    """
    try:
        num = int(num_str)
        bin(num)
        hex(num)
        oct(num)
        return True
    except ValueError:
        return False

def on_click(event):
    """
    Função para lidar com o evento de clique nos botões da calculadora.
    """
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "Del":
        entry.delete(0, tk.END)
    elif text == "Dec > Bin":
        if check_conversion(entry.get()):
            num = int(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, bin(num)[2:])
        else:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Invalid Input")
    elif text == "Dec > Hex":
        if check_conversion(entry.get()):
            num = int(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, hex(num)[2:])
        else:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Invalid Input")
    elif text == "Dec > Octal":
        if check_conversion(entry.get()):
            num = int(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, oct(num)[2:])
        else:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Invalid Input")
    elif text == "Bin/Hex/Oct > Dec":
        os.system("python calculadora2.py")  # Chama o arquivo "calculadora2.py"
    else:
        entry.insert(tk.END, text)

root = tk.Tk()  # Cria a janela principal do aplicativo
root.title("Calculadora")  # Define o título da janela

entry = tk.Entry(root, width=30, borderwidth=5)  # Cria uma caixa de entrada para exibir e inserir texto
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)  # Posiciona a caixa de entrada na janela

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'Del', '0', '=', '+',
    'Dec > Bin', 'Dec > Hex', 'Dec > Octal',
    'Bin/Hex/Oct > Dec'
]

row = 1
col = 0

for button_text in buttons:  # Loop para criar e posicionar os botões na janela
    button = tk.Button(root, text=button_text, padx=20, pady=10)  # Cria um botão com o texto fornecido
    button.grid(row=row, column=col, padx=5, pady=5)  # Posiciona o botão na janela

    button.bind("<Button-1>", on_click)  # Associa a função on_click ao evento de clique do botão

    col += 1
    if col > 3:  # Move para a próxima linha após adicionar 4 botões por linha
        col = 0
        row += 1

root.mainloop()  # Inicia o loop principal da aplicação para escutar eventos