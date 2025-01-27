import tkinter as tk

janela = tk.Tk()

janela.title("REPUST RPG")
janela.geometry("1000x900")
janela.configure(bg="#A67C58", pady=100)

label_logo = tk.Label(janela, text="REPUST", fg="#4EA68D", bg="#A67C58", font=("Agency FB", 100, "bold"))
label_logo.pack()

label = tk.Label(janela, text="RPG", fg="#F2994B", bg="#A67C58", font=("Agency FB", 20, "bold"))
label.pack()

## ------

botao_new = tk.Button(janela, text="NOVO JOGO", bg="#4EA68D", font=("Agency FB", 20), fg="white", bd=5, relief="ridge")
botao_new.pack(pady=10)

botao_new = tk.Button(janela, text="CARREGAR JOGO", bg="#4EA68D", font=("Agency FB", 20), fg="white", bd=5, relief="ridge")
botao_new.pack(pady=10)

botao_new = tk.Button(janela, text="CONFIGURAÇÕES", bg="#4EA68D", font=("Agency FB", 20), fg="white", bd=5, relief="ridge")
botao_new.pack(pady=10)

botao_new = tk.Button(janela, text="SAIR", bg="#4EA68D", font=("Agency FB", 20), fg="white", bd=5, relief="ridge")
botao_new.pack(pady=10)

label_creditos = tk.Label(janela, text="@rodrigo_silva @vinicius_almeida", fg="white", bg="#A67C58", font=("Agency FB", 10, "bold"))
label_creditos.pack(side="bottom")

janela.mainloop()