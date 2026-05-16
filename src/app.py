import requests

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

def mostrar_frase():
    try:
        resposta = requests.get("https://zenquotes.io/api/random")

        dados = resposta.json()

        frase = dados[0]["q"]
        autor = dados[0]["a"]

        traducoes = {
            "Thinking is difficult, that's why most people judge.": "Pensar é difícil, por isso a maioria das pessoas julga.",
            "Perhaps the most tragic thing about mankind is that we are all dreaming about some magical garden over the horizon, instead of enjoying the roses that are right outside today.": "Talvez a coisa mais trágica da humanidade seja que todos sonham com um jardim mágico no horizonte, em vez de aproveitar as rosas que estão logo aqui hoje."
        }

        frase_traduzida = traducoes.get(frase, frase)

        return f'"{frase_traduzida}" - {autor}'

    except Exception as erro:
        return f"Erro: {erro}"
def menu():
    while True:
        print("\n1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Remover tarefa")
        print("4 - Mostrar frase motivacional")
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

        elif opcao == "4":
            print(mostrar_frase())

        elif opcao == "0":
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    menu()