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
        

    def receber_dano(self, quantidade : int):
        if not self.estar_vivo or quantidade <=0:
            return

        dano_efetivo = max(1, quantidade - self.armadura)
        self.vida -= max(0,self.vida - dano_efetivo)
        print(f"{self.__class__.__name__} recebeu {dano_efetivo} de dano! Vida restante: {self.vida}")

        if not self.estar_vivo:
            print(f"{self.nome} Morreu")

    def atacar(self, alvo):
        if self.esta_vivo:     
            alvo.receber_dano(self.dano)
        else:
            print(f"{self.__class__.__name__} não pode atacar porque está morto.")

    def estar_vivo(self):
        return self.vida > 0

    def movimentacao(self, direcao_x:float, direcao_y:float, dt:float):
        if not self.estar_vivo:
            return
        comprimento = (direcao_x ** 2 +direcao_y ** 2) ** 0.5
        if comprimento == 0:
            return
        self.x +=(direcao_x / comprimento) * self.velocidade * dt
        self.y +=(direcao_y / comprimento) * self.velocidade * dt


    @abstractmethod
    def atualizar(self, dt):
        pass

class Jogador(Boneco):

    def __init__(self, nome : str, x : float, y : float, dano : int = 10,):
        super().__init__(nome=nome, x=x, y=y, dano=dano)
        self.dinheiro = 5


    def recarregar_arma(self):
        return

    def comprar_arma(self):
        return

    def trocar_arma(self):
        return

class Npc(Boneco):
    def __init__(self, nome : str, x : float, y : float, vida : int, armadura : int, dano : int, velocidade : float):
        super().__init__(nome=nome, x=x, y=y, vida=vida, armadura=armadura, dano=dano, velocidade=velocidade)


class Inimigo(Boneco):
    def __init__(self, nome : str, x : float, y : float, vida : int, armadura : int, dano : int, velocidade : float):
        super().__init__(nome=nome, x=x, y=y, vida=vida, armadura=armadura, dano=dano, velocidade=velocidade)

    


