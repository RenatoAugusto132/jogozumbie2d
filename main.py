from personagens import Jogador, Inimigo
from armas import MP5

if __name__ == "__main__":

    jogador = Jogador("Jogador A", x=0, y=0, dano=10)
    
    arma = MP5()
    jogador.equipar_arma(arma)

    zumbis = [
        Inimigo("Zumbi Comum", x=0, y=0, vida=35, armadura=0, dano=10, velocidade=1.0),
        Inimigo("Zumbi Blindado", x=0, y=0, vida=50, armadura=5, dano=30, velocidade=0.8),
        Inimigo("Zumbi Mutante", x=0, y=0, vida=80, armadura=2, dano=15, velocidade=1.2)
    ]

    while True:
        zumbis_vivos = [z for z in zumbis if z.esta_vivo()]

        if not zumbis_vivos:
            print("Parabéns! Todos os zumbis foram eliminados!")
            break

        print("\n--- INIMIGOS DISPONÍVEIS ---")
        for i, zumbi in enumerate(zumbis_vivos):
            print(f"[{i + 1}] {zumbi.nome} | Vida: {zumbi.vida} | Armadura: {zumbi.armadura}")

        print("[0] Sair do teste")
        
        escolha = input("\nEscolha o número do zumbi para atirar: ")
        
        if not escolha.isdigit():
            print("Digite um número válido!")
            continue

        numero = int(escolha)

        if numero == 0:
            print("Encerrando o teste...")
            break
        
        indice = numero - 1
        if 0 <= indice < len(zumbis_vivos):
            print("\n" + "-" * 30)
            jogador.atirar_em(zumbis_vivos[indice])
            print("-" * 30)
        else:
            print("Opção inválida!")