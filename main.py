import tkinter as tk
from tkinter import messagebox
import random
import string

# Função para gerar a senha - Atende ao critério de 'funções integradas'
def gerar_senha():
    try:
        tamanho = int(entry_tamanho.get())
        if tamanho < 4:
            messagebox.showwarning("Aviso", "O tamanho mínimo é de 4 caracteres.")
            return
        
        # Uso de bibliotecas padrão (string e random)
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = "".join(random.choice(caracteres) for _ in range(tamanho))
        
        # Atualiza a interface com a senha gerada
        entry_senha.delete(0, tk.END)
        entry_senha.insert(0, senha)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número inteiro para o tamanho.")

# Configuração da Interface Gráfica (Tkinter)
root = tk.Tk()
root.title("Python Pro: Gerador de Senhas")
root.geometry("350x250")

label_titulo = tk.Label(root, text="Gerador de Senhas Seguras", font=("Arial", 12, "bold"))
label_titulo.pack(pady=10)

label_instrucao = tk.Label(root, text="Digite o tamanho da senha:")
label_instrucao.pack()

entry_tamanho = tk.Entry(root)
entry_tamanho.pack(pady=5)

btn_gerar = tk.Button(root, text="Gerar Senha", command=gerar_senha)
btn_gerar.pack(pady=10)

entry_senha = tk.Entry(root, font=("Arial", 10), justify='center', width=30)
entry_senha.pack(pady=10)

root.mainloop()
