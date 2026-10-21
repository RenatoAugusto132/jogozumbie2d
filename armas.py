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