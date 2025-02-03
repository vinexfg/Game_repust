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
    
        














    
# class classe_do_personagem:

#     def guerreiro(self):
#         dano = 15
#         defesa = 10
#         vidas = 120


        
        

