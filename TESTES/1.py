import tkinter as tk

##  Menu Inicial
def frame1():
    for widget in janela.winfo_children():
        widget.destroy()

    frame_menu = tk.Frame(janela, bg="#A67C58")
    frame_menu.pack(fill="both", expand=True)

    def sairJogo():
        janela.destroy()

    ##----------------------------------------------------------------------------------------
    ## FRAME MENU

    label_logo = tk.Label(frame_menu, text="REPUST", fg="#4EA68D", bg="#A67C58", font=("Agency FB", 100, "bold"))
    label_logo.pack()

    label = tk.Label(frame_menu, text="RPG", fg="#F2994B", bg="#A67C58", font=("Agency FB", 20, "bold"))
    label.pack()

    ##------

    botao_novo = tk.Button(frame_menu, text="NOVO JOGO", bg="#4EA68D", font=("Agency FB", 20), fg="#F2F2F2", bd=5, relief="ridge", command=frame2)
    botao_novo.pack(pady=10)

    botao_carregar = tk.Button(frame_menu, text="CARREGAR JOGO", bg="#4EA68D", font=("Agency FB", 20), fg="#F2F2F2", bd=5, relief="ridge", command=frame3)
    botao_carregar.pack(pady=10)

    botao_conf = tk.Button(frame_menu, text="CONFIGURAÇÕES", bg="#4EA68D", font=("Agency FB", 20), fg="#F2F2F2", bd=5, relief="ridge", command=frame4)
    botao_conf.pack(pady=10)

    botao_sair = tk.Button(frame_menu, text="SAIR", bg="#4EA68D", font=("Agency FB", 20), fg="#F2F2F2", bd=5, relief="ridge", command=sairJogo)
    botao_sair.pack(pady=10)

    label_creditos = tk.Label(frame_menu, text="@rodrigo_silva @vinicius_almeida", fg="#F2F2F2", bg="#A67C58", font=("Agency FB", 10, "bold"))
    label_creditos.pack(side="bottom")

    ##----------------------------------------------------------------------------------------

##  Menu Novo Jogo
def frame2():
    for widget in janela.winfo_children():
        widget.destroy()

    frame_novo = tk.Frame(janela, bg="#A67C58")
    frame_novo.pack(fill="both", expand=True)

    ##--------------------------------------------------------

    personagem = {"nome": "indefinido", "classe": "indefinido", "raca": "indefinido" ,"sexo": "indefinido"}

    ## --- Classe

    def pegarGuerreiro():
        personagem["classe"] = "guerreiro"
        classe1.config(bg="#F2994B", fg="#F2F2F2")
        classe2.config(fg="#4EA68D", bg="#F2F2F2")
        classe3.config(fg="#4EA68D", bg="#F2F2F2")
        classe4.config(fg="#4EA68D", bg="#F2F2F2")

    def pegarMago():
        personagem["classe"] = "mago"
        classe2.config(bg="#F2994B", fg="#F2F2F2")
        classe1.config(fg="#4EA68D", bg="#F2F2F2")
        classe3.config(fg="#4EA68D", bg="#F2F2F2")
        classe4.config(fg="#4EA68D", bg="#F2F2F2")
        
    def pegarLadino():
        personagem["classe"] = "ladino"
        classe3.config(bg="#F2994B", fg="#F2F2F2")
        classe2.config(fg="#4EA68D", bg="#F2F2F2")
        classe1.config(fg="#4EA68D", bg="#F2F2F2")
        classe4.config(fg="#4EA68D", bg="#F2F2F2")
       
    def pegarBarbaro():
        personagem["classe"] = "barbaro"
        classe4.config(bg="#F2994B", fg="#F2F2F2")
        classe2.config(fg="#4EA68D", bg="#F2F2F2")
        classe3.config(fg="#4EA68D", bg="#F2F2F2")
        classe1.config(fg="#4EA68D", bg="#F2F2F2")
        
    ## --- Raça

    def pegarHumano():
        personagem["raca"] = "humano"
        raca1.config(bg="#F2994B", fg="#F2F2F2")
        raca2.config(fg="#4EA68D", bg="#F2F2F2")
        raca3.config(fg="#4EA68D", bg="#F2F2F2")
        raca4.config(fg="#4EA68D", bg="#F2F2F2")

    def pegarElfo():
        personagem["raca"] = "elfo"
        raca2.config(bg="#F2994B", fg="#F2F2F2")
        raca1.config(fg="#4EA68D", bg="#F2F2F2")
        raca3.config(fg="#4EA68D", bg="#F2F2F2")
        raca4.config(fg="#4EA68D", bg="#F2F2F2")
        
    def pegarAnao():
        personagem["raca"] = "anao"
        raca3.config(bg="#F2994B", fg="#F2F2F2")
        raca2.config(fg="#4EA68D", bg="#F2F2F2")
        raca1.config(fg="#4EA68D", bg="#F2F2F2")
        raca4.config(fg="#4EA68D", bg="#F2F2F2")
       
    def pegarOrc():
        personagem["raca"] = "orc"
        raca4.config(bg="#F2994B", fg="#F2F2F2")
        raca2.config(fg="#4EA68D", bg="#F2F2F2")
        raca3.config(fg="#4EA68D", bg="#F2F2F2")
        raca1.config(fg="#4EA68D", bg="#F2F2F2")

    ## -- Sexo

    def pegarMasculino():
        personagem["sexo"] = "masculino"
        sexo1.config(bg="#F2994B", fg="#F2F2F2")
        sexo2.config(fg="#4EA68D", bg="#F2F2F2")
        
    def pegarFeminino():
        personagem["sexo"] = "feminino"
        sexo2.config(bg="#F2994B", fg="#F2F2F2")
        sexo1.config(fg="#4EA68D", bg="#F2F2F2")
           
    
    ##--------------------------------------------------------


    ##----------------------------------------------------------------------------------------
    ## FRAME NOVO

    label_logo = tk.Label(frame_novo, text="NOVO JOGO", fg="#4EA68D", bg="#A67C58", font=("Agency FB", 75, "bold"))
    label_logo.pack()

    label = tk.Label(frame_novo, text="Criação de personagem", fg="#F2994B", bg="#A67C58", font=("Agency FB", 25, "bold"))
    label.pack()


    label_nome = tk.Label(frame_novo, text="NOME DO PERSONAGEM", fg="#F2F2F2", bg="#A67C58", font=("Agency FB", 15, "bold"))
    label_nome.pack()

    caixa_nome = tk.Text(frame_novo, fg="#4EA68D", bg="#F2F2F2", font=("Agency FB", 15, "bold"),  width=40, height=0)
    caixa_nome.pack()

    grupo_classes = tk.Frame(frame_novo, bg="#A67C58")
    grupo_classes.pack()

    grupo_raca = tk.Frame(frame_novo, bg="#A67C58")
    grupo_raca.pack()

    ##---

    label_classe = tk.Label(grupo_classes, text="CLASSE DO PERSONAGEM", fg="#F2F2F2", bg="#A67C58", font=("Agency FB", 15, "bold"))
    label_classe.pack()
    
    classe1 = tk.Button(grupo_classes, text="GUERREIRO", width=20, height=0, fg="#4EA68D", bg="#F2F2F2", font=("Agency FB", 15, "bold"), bd=5, relief="ridge", command=pegarGuerreiro)
    classe1.pack( pady=2, padx=5, side="left")

    classe2 = tk.Button(grupo_classes, text="MAGO", width=20, height=0, fg="#4EA68D", bg="#F2F2F2", font=("Agency FB", 15, "bold"), bd=5, relief="ridge", command=pegarMago)
    classe2.pack(pady=2, padx=5, side="left")

    classe3 = tk.Button(grupo_classes, text="LADINO", width=20, height=0, fg="#4EA68D", bg="#F2F2F2", font=("Agency FB", 15, "bold"), bd=5, relief="ridge", command=pegarLadino)
    classe3.pack(pady=2, padx=5, side="left")

    classe4 = tk.Button(grupo_classes, text="BÁRBARO", width=20, height=0, fg="#4EA68D", bg="#F2F2F2", font=("Agency FB", 15, "bold"), bd=5, relief="ridge", command=pegarBarbaro)
    classe4.pack(pady=2, padx=5, side="left")

    ##---

    label_raca = tk.Label(grupo_raca, text="RAÇA DO PERSONAGEM", fg="#F2F2F2", bg="#A67C58", font=("Agency FB", 15, "bold"))
    label_raca.pack()

    raca1 = tk.Button(grupo_raca, text="HUMANO", width=20, height=0, fg="#4EA68D", bg="#F2F2F2", font=("Agency FB", 15, "bold"), bd=5, relief="ridge", command=pegarHumano)
    raca1.pack( pady=2, padx=5, side="left")

    raca2 = tk.Button(grupo_raca, text="ELFO", width=20, height=0, fg="#4EA68D", bg="#F2F2F2", font=("Agency FB", 15, "bold"), bd=5, relief="ridge", command=pegarElfo)
    raca2.pack(pady=2, padx=5, side="left")

    raca3 = tk.Button(grupo_raca, text="ANÃO", width=20, height=0, fg="#4EA68D", bg="#F2F2F2", font=("Agency FB", 15, "bold"), bd=5, relief="ridge", command=pegarAnao)
    raca3.pack(pady=2, padx=5, side="left")

    raca4 = tk.Button(grupo_raca, text="ORC", width=20, height=0, fg="#4EA68D", bg="#F2F2F2", font=("Agency FB", 15, "bold"), bd=5, relief="ridge", command=pegarOrc)
    raca4.pack(pady=2, padx=5, side="left")

    ##---
    
    label_sexo = tk.Label(frame_novo, text="SEXO DO PERSONAGEM", fg="#F2F2F2", bg="#A67C58", font=("Agency FB", 15, "bold"))
    label_sexo.pack()

    sexo1 = tk.Button(frame_novo, text="MASCULINO", width=20, height=0, fg="#4EA68D", bg="#F2F2F2", font=("Agency FB", 15, "bold"), bd=5, relief="ridge", command=pegarMasculino)
    sexo1.pack(pady=2, padx=5)

    sexo2 = tk.Button(frame_novo, text="FEMININO", width=20, height=0, fg="#4EA68D", bg="#F2F2F2", font=("Agency FB", 15, "bold"), bd=5, relief="ridge", command=pegarFeminino)
    sexo2.pack(pady=2, padx=5)

    botao_criar = tk.Button(frame_novo, text="Criar Personagem", bg="#4EA68D", font=("Agency FB", 15), fg="white", bd=5, relief="ridge")
    botao_criar.pack(pady=10)


    botao_voltar = tk.Button(frame_novo, text="Voltar", bg="#4EA68D", font=("Agency FB", 15), fg="white", bd=5, relief="ridge", command=frame1)
    botao_voltar.pack(pady=10, side="bottom")

    ## Escolher Save de Salvamento

    def novoSave():
        for widget in janela.winfo_children():
            widget.destroy()
        frame_salvar = tk.Frame(janela, bg="#A67C58")
        frame_salvar.pack(fill="both", expand=True)


    ##----------------------------------------------------------------------------------------

##  Menu Carregar Jogo
def frame3():
    for widget in janela.winfo_children():
        widget.destroy()

    frame_carregar = tk.Frame(janela, bg="#A67C58")
    frame_carregar.pack(fill="both", expand=True)

    selecionado = {"Escolhido": "indefinido"}

    def escolherSave1():
        selecionado["Escolhido"] = "save1"
        save1.config(bg="#F2994B", fg="#F2F2F2")
        save2.config(fg="#4EA68D", bg="#F2F2F2")
        save3.config(fg="#4EA68D", bg="#F2F2F2")
        save4.config(fg="#4EA68D", bg="#F2F2F2")
    
    def escolherSave2():
        selecionado["Escolhido"] = "save2"
        save2.config(bg="#F2994B", fg="#F2F2F2")
        save1.config(fg="#4EA68D", bg="#F2F2F2")
        save3.config(fg="#4EA68D", bg="#F2F2F2")
        save4.config(fg="#4EA68D", bg="#F2F2F2")
    
    def escolherSave3():
        selecionado["Escolhido"] = "save3"
        save3.config(bg="#F2994B", fg="#F2F2F2")
        save2.config(fg="#4EA68D", bg="#F2F2F2")
        save1.config(fg="#4EA68D", bg="#F2F2F2")
        save4.config(fg="#4EA68D", bg="#F2F2F2")
    
    def escolherSave4():
        selecionado["Escolhido"] = "save4"
        save4.config(bg="#F2994B", fg="#F2F2F2")
        save2.config(fg="#4EA68D", bg="#F2F2F2")
        save3.config(fg="#4EA68D", bg="#F2F2F2")
        save1.config(fg="#4EA68D", bg="#F2F2F2")
        

    label_logo = tk.Label(frame_carregar, text="CARREGAR JOGO", fg="#4EA68D", bg="#A67C58", font=("Agency FB", 75, "bold"))
    label_logo.pack()

    label = tk.Label(frame_carregar, text="Jogos salvos", fg="#F2994B", bg="#A67C58", font=("Agency FB", 25, "bold"))
    label.pack()

    save1 = tk.Button(frame_carregar, text="JOGO SALVO 01", width=50, height=0, fg="#4EA68D", bg="#F2F2F2", font=("Agency FB", 15, "bold"), bd=5, relief="ridge", command=escolherSave1)
    save1.pack(pady=10, padx=5)

    save2 = tk.Button(frame_carregar, text="JOGO SALVO 02", width=50, height=0, fg="#4EA68D", bg="#F2F2F2", font=("Agency FB", 15, "bold"), bd=5, relief="ridge", command=escolherSave2)
    save2.pack(pady=10, padx=5)

    save3 = tk.Button(frame_carregar, text="JOGO SALVO 03", width=50, height=0, fg="#4EA68D", bg="#F2F2F2", font=("Agency FB", 15, "bold"), bd=5, relief="ridge", command=escolherSave3)
    save3.pack(pady=10, padx=5)

    save4 = tk.Button(frame_carregar, text="JOGO SALVO 04", width=50, height=0, fg="#4EA68D", bg="#F2F2F2", font=("Agency FB", 15, "bold"), bd=5, relief="ridge", command=escolherSave4)
    save4.pack(pady=10, padx=5)

    botao_carregar = tk.Button(frame_carregar, text="Carregar", bg="#4EA68D", font=("Agency FB", 15), fg="white", bd=5, relief="ridge")
    botao_carregar.pack(pady=10)

    botao_voltar = tk.Button(frame_carregar, text="Voltar", bg="#4EA68D", font=("Agency FB", 15), fg="white", bd=5, relief="ridge", command=frame1)
    botao_voltar.pack(pady=10, side="bottom")

##  Menu Configurações
def frame4():
    for widget in janela.winfo_children():
        widget.destroy()

    frame_conf = tk.Frame(janela, bg="#A67C58")
    frame_conf.pack(fill="both", expand=True)

    

    label_logo = tk.Label(frame_conf, text="CONFIGURAÇÕES", fg="#4EA68D", bg="#A67C58", font=("Agency FB", 75, "bold"))
    label_logo.pack()

    label = tk.Label(frame_conf, text="Configuração do jogo", fg="#F2994B", bg="#A67C58", font=("Agency FB", 25, "bold"))
    label.pack()


    botao_voltar = tk.Button(frame_conf, text="Voltar", bg="#4EA68D", font=("Agency FB", 15), fg="white", bd=5, relief="ridge", command=frame1)
    botao_voltar.pack(pady=10, side="bottom")







## Janela Principal
janela = tk.Tk()

janela.title("REPUST RPG")
janela.geometry("1000x900")
janela.configure(bg="#A67C58", pady=100)

frame1()

janela.mainloop()