from abc import ABC, abstractmethod

class Boneco(ABC):
    nome = str
    def __init__(self, nome : str, x : float, y : float, vida : int = 100, armadura : int = 0, dano : int = 5, velocidade : float = 2.0):
        self.nome = nome
        self.x = x
        self.y = y
        self.vida = vida
        self.armadura = armadura
        self.dano = dano
        self.velocidade = velocidade
        self.esta_vivo = True

    def receber_dano(self, quantidade : int):
        dano_efetivo = max(1, quantidade - self.armadura)
        self.vida -= dano_efetivo
        print(f"{self.__class__.__name__} recebeu {dano_efetivo} de dano! Vida restante: {self.vida}")

    def atacar(self, alvo):
        if self.esta_vivo:     
            alvo.receber_dano(self.dano)
        else:
            print(f"{self.__class__.__name__} não pode atacar porque está morto.")

class Jogador(Boneco):
    def __init__(self, nome : str, x : float, y : float, dano : int = 10):
        super().__init__(nome=nome, x=x, y=y, dano=dano)

class Npc(Boneco):
    def __init__(self, nome : str, x : float, y : float, vida : int, armadura : int, dano : int, velocidade : float):
        super().__init__(nome=nome, x=x, y=y, vida=vida, armadura=armadura, dano=dano, velocidade=velocidade)


class Zumbi(Boneco):
    def __init__(self, nome : str, x : float, y : float, vida : int, armadura : int, dano : int, velocidade : float):
        super().__init__(nome=nome, x=x, y=y, vida=vida, armadura=armadura, dano=dano, velocidade=velocidade)
