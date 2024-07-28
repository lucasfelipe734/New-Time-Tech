import tkinter as tk
import subprocess


def binario_para_decimal():
    try:
        numero_binario = entrada.get()
        decimal = int(numero_binario, 2)
        resultado.config(text="O número em decimal é: " + str(decimal))
    except ValueError:
        resultado.config(text="Erro: Por favor, digite um número binário válido.")

def hexadecimal_para_decimal():
    try:
        numero_hexadecimal = entrada.get()
        decimal = int(numero_hexadecimal, 16)
        resultado.config(text="O número em decimal é: " + str(decimal))
    except ValueError:
        resultado.config(text="Erro: Por favor, digite um número hexadecimal válido.")

def octal_para_decimal():
    try:
        numero_octal = entrada.get()
        decimal = int(numero_octal, 8)
        resultado.config(text="O número em decimal é: " + str(decimal))
    except ValueError:
        resultado.config(text="Erro: Por favor, digite um número octal válido.")

def executar_script():
    subprocess.Popen(["python", "main.py"])

root = tk.Tk()
root.title("Conversão para decimal")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Digite o número:")
label.grid(row=0, column=0, columnspan=2, pady=5)

entrada = tk.Entry(frame)
entrada.grid(row=1, column=0, columnspan=2, pady=5)

botao_binario = tk.Button(frame, text="Binário para Decimal", command=binario_para_decimal)
botao_binario.grid(row=2, column=0, columnspan=2, pady=5)

botao_hexadecimal = tk.Button(frame, text="Hexadecimal para Decimal", command=hexadecimal_para_decimal)
botao_hexadecimal.grid(row=3, column=0, columnspan=2, pady=5)

botao_octal = tk.Button(frame, text="Octal para Decimal", command=octal_para_decimal)
botao_octal.grid(row=4, column=0, columnspan=2, pady=5)

resultado = tk.Label(frame, text="")
resultado.grid(row=5, column=0, columnspan=2, pady=5)

botao_executar = tk.Button(frame, text="Calculadora Decimal", command=executar_script)
botao_executar.grid(row=6, column=0, columnspan=2, pady=5)

root.mainloop()
