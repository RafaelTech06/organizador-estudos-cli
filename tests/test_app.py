from src.app import adicionar_tarefa, listar_tarefas, remover_tarefa, tarefas

def setup_function():
    tarefas.clear()

def test_adicionar_tarefa():
    resultado = adicionar_tarefa("Estudar Python")
    assert resultado == "Tarefa adicionada"
    assert "Estudar Python" in tarefas

def test_tarefa_vazia():
    resultado = adicionar_tarefa("")
    assert resultado == "Erro: tarefa vazia"

def test_remover_tarefa_invalida():
    resultado = remover_tarefa(0)
    assert resultado == "Erro: índice inválido"