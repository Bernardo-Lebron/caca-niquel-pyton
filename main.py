import random
import time
import os

def slot_machine():
    frutas = ["🍒", "🍋", "🍊", "🍇", "🍉", "🍌"]

    premios = {
        "🍒": 5,
        "🍋": 10,
        "🍊": 50,
        "🍇": 15,
        "🍉": 20,
        "🍌": 30
    }

    saldo = 20
    custo = 1

    print("🎰 Bem-vindo ao Caça-Níquel! 🎰")
    print("Tabela de prêmios (3 iguais):")
    for fruta, premio in premios.items():
        print(f"{fruta} → {premio} moedas")
    print(f"\nVocê começa com {saldo} moedas.\n")

    while saldo > 0:
        jogar = input("Pressione ENTER para girar (ou digite 'sair' para encerrar): ")
        if jogar.lower() == "sair":
            break

        saldo -= custo
        print(f"\n💰 Saldo atual: {saldo} moedas")

        print("Girando...\n")

        for _ in range(15):  # número de "giros" animados
            giro = [random.choice(frutas) for _ in range(3)]
            print(" ".join(giro), end="\r", flush=True)  
            time.sleep(0.1)

        # Resultado final
        resultado = [random.choice(frutas) for _ in range(3)]
        print(" ".join(resultado))  

        # Verifica vitória
        if resultado[0] == resultado[1] == resultado[2]:
            ganho = premios[resultado[0]]
            saldo += ganho
            print(f"🎉 PARABÉNS! Você ganhou {ganho} moedas! 🎉")
        else:
            print("💔 Não foi dessa vez, tente novamente!")

        print(f"💰 Saldo atual: {saldo} moedas\n")

    print("\n🔚 Jogo encerrado!")
    print(f"Você terminou com {saldo} moedas.")
if __name__ == "__main__":

    slot_machine()

