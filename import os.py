import os
from datetime import datetime


def limpar_tela():
    """Limpa o terminal pois evita de deixar muita coisa no terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    """Pausa para o usuário ler a informação."""
    input("\nPressione ENTER para continuar...")


def adicionar_tarefa():
    """Ao adicionar uma tarefa mostrará tanto hora e data de adição da tarefa."""
    limpar_tela()
    print("=== ADICIONAR TAREFA ===")

    tarefa = input("Digite a tarefa: ")
    data = datetime.now().strftime("%d/%m/%Y %H:%M")

    registro = f"[ ] | {data} | {tarefa}\n"

    with open("tarefas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(registro)

    print("\n Tarefa adicionada com sucesso!")
    pausar()


def listar_tarefas():
    """Lista todas as tarefas numeradas."""
    limpar_tela()
    print("=== LISTA DE TAREFAS ===")

    try:
        with open("tarefas.txt", "r", encoding="utf-8") as arquivo:
            tarefas = arquivo.readlines()

            if not tarefas:
                print("\n Nenhuma tarefa cadastrada.")
                pausar()
                return []

            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i} - {tarefa.strip()}")

            pausar()
            return tarefas

    except FileNotFoundError:
        print("\n Nenhuma tarefa cadastrada ainda.")
        pausar()
        return []


def concluir_tarefa():
    """Marca uma tarefa como concluída."""
    tarefas = listar_tarefas()
    if not tarefas:
        return

    try:
        """Pede ao usuário o número da tarefa que ele quer concluir"""
        numero = int(input("\nDigite o número da tarefa concluída: "))

        """Verifica se o número está dentro do tamanho da lista"""
        if 1 <= numero <= len(tarefas):

            """Checa se a tarefa já foi concluída antes"""
            if "[✔]" in tarefas[numero - 1]:
                print("\n Tarefa já está concluída.")
            else:
                tarefas[numero - 1] = tarefas[numero - 1].replace("[ ]", "[✔]")

                """Salva todas as tarefas novamente no arquivo só que atualizado"""
                with open("tarefas.txt", "w", encoding="utf-8") as arquivo:
                    arquivo.writelines(tarefas)

                print("\n Tarefa marcada como concluída!")
        else:
            print("\n Número inválido.")

    except ValueError:
        print("\n Digite um número válido.")

    pausar()


def remover_tarefa():
    """Remove uma tarefa."""
    tarefas = listar_tarefas()
    if not tarefas:
        return

    try:
        numero = int(input("\nDigite o número da tarefa a remover: "))

        if 1 <= numero <= len(tarefas):
            tarefas.pop(numero - 1)

            with open("tarefas.txt", "w", encoding="utf-8") as arquivo:
                arquivo.writelines(tarefas)

            print("\n Tarefa removida com sucesso!")
        else:
            print("\n Número inválido.")

    except ValueError:
        print("\n Digite um número válido.")

    pausar()


def menu():
    """Menu principal do sistema."""
    while True:
        limpar_tela()
        print("===== SISTEMA DE TAREFAS =====")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("5 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            remover_tarefa()
        elif opcao == "5":
            limpar_tela()
            print("Encerrando o sistema...")
            break
        else:
            print("\n Opção inválida!")
            pausar()


# Execução do sistema
menu()
