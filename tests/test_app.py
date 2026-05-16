from src.app import (
    adicionar_tarefa,
    listar_tarefas,
    remover_tarefa,
    tarefas,
)


def setup_function():
    tarefas.clear()


def test_adicionar_tarefa():
    resultado = adicionar_tarefa("Estudar Python")

    assert resultado == "Tarefa adicionada"
    assert "Estudar Python" in tarefas


def test_tarefa_vazia():
    resultado = adicionar_tarefa("")

    assert resultado == "Erro: tarefa vazia"
    assert len(tarefas) == 0


def test_listar_tarefas_vazia():
    resultado = listar_tarefas()

    assert resultado == "Nenhuma tarefa cadastrada"


def test_listar_tarefas_com_itens():
    adicionar_tarefa("Estudar Python")
    adicionar_tarefa("Fazer exercícios")

    resultado = listar_tarefas()

    assert "1. Estudar Python" in resultado
    assert "2. Fazer exercícios" in resultado


def test_remover_tarefa_valida():
    adicionar_tarefa("Estudar Python")

    resultado = remover_tarefa(0)

    assert resultado == "Tarefa removida"
    assert "Estudar Python" not in tarefas


def test_remover_tarefa_invalida():
    resultado = remover_tarefa(0)

    assert resultado == "Erro: índice inválido"


def test_estado_apos_operacoes():
    adicionar_tarefa("A")
    adicionar_tarefa("B")
    remover_tarefa(0)

    assert tarefas == ["B"]