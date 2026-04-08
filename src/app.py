tarefas = []

def adicionar_tarefa(nome):
    if not nome:
        return "Erro: tarefa vazia"
    tarefas.append(nome)
    return "Tarefa adicionada"

def listar_tarefas():
    if not tarefas:
        return "Nenhuma tarefa cadastrada"
    return "\n".join(f"{i+1}. {t}" for i, t in enumerate(tarefas))

def remover_tarefa(indice):
    if indice < 0 or indice >= len(tarefas):
        return "Erro: índice inválido"
    tarefas.pop(indice)
    return "Tarefa removida"

def menu():
    while True:
        print("\n1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Remover tarefa")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Digite a tarefa: ")
            print(adicionar_tarefa(nome))

        elif opcao == "2":
            print(listar_tarefas())

        elif opcao == "3":
            try:
                indice = int(input("Número da tarefa: ")) - 1
                print(remover_tarefa(indice))
            except:
                print("Erro: entrada inválida")

        elif opcao == "0":
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    menu()