class Arma:
    def __init__(self, nome, dano, capacidade_pente,
        municao_reserva, tempo_recarga, preco):
        self.nome = nome
        self.dano = dano
        self.capacidade_pente = capacidade_pente
        self.municao_reserva = municao_reserva
        self.tempo_recarga = tempo_recarga
        self.preco = preco
        self.recarregando = False
        self.tempo_restante = 0

def atirar(self):
    if self.recarregando:
        return False

    if self.municao_no_pente <= 0:
        print(f"{self.nome} está sem munição! Recarregue a arma.")
        return False

    self.municao_no_pente -= 1
    return True

def iniciar_recarga(self):
    if self.recarregando:
        return False

    if self.municao_no_pente == self.capacidade_pente:
        return False

    if self.municao_reserva <= 0:
        return False

    self.recarregando = True
    self.tempo_restante = self.tempo_recarga
    return True

def atualizar(self, dt):
    if not self.recarregando:
        return

    self.tempo_restante = max(0, self.tempo_restante - dt)

    if self.tempo_restante == 0:
        faltam = self.capacidade_pente - self.municao_no_pente

        quantidade = min(faltam, self.municao_reserva)

        self.municao_no_pente += quantidade
        self.municao_reserva -= quantidade
        self.recarregando = False
    
    