print('TESTES')


class Personagem:
    def __init__(self, nome, sexo) -> None:
        self.nome = nome
        self.sexo = sexo
        self.dano = 5
        self.defesa = 2.5
        self.lv = 1
        self.xp = 5
        self.vida = 100
        self.classe = ['fogo', 'agua', 'terra', 'ar']
    

    def __str__(self) -> str:
        return (f'Nome: {self.nome}\n'
                f'Sexo: {self.sexo}\n'
                f'Classe: {self.classe}\n'
                f'Ataque: {self.dano}\n'
                f'Defesa: {self.defesa}\n'
                f'Nível: {self.lv}\n'
                f'Vida: {self.vida}\n')
    
    
    #criar um arquivo de erro. 

    def personagem_base(self):
        self.nome = input('Nome: ')
        self.sexo = input('Sexo M/F : ')
    
    def armazem_dados(self):
        Personagem_dict  = {
            "nome": self.nome,
            "sexo": self.sexo,
            "saude": self.defesa,
            "classe": self.classe,
            "ataque": self.dano,
            "defesa": self.defesa,
            "nivel": self.lv

        }
        return Personagem_dict
    
guerreiro = Personagem("Arthas", "Guerreiro")
print(guerreiro)
    
        














    
# class classe_do_personagem:

#     def guerreiro(self):
#         dano = 15
#         defesa = 10
#         vidas = 120


        
        

