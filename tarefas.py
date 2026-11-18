import json
import os

ARQUIVO = 'tarefas.json'


def carregar_tarefas():
    if not os.path.exists(ARQUIVO):
        return[]
    with open(ARQUIVO, 'r', encoding = 'utf-8') as f:
        return json.load(f)


def salvar_tarefas(tarefas):
    with open(ARQUIVO, 'w', encoding = 'utf-8') as f:
        json.dump(tarefas, f, ensure_ascii=False, indent = 2)

def adicionar_tarefa(tarefas):
    titulo = input('Digite a tarefa:').strip()
    if not titulo:
        print('A tarefa não pode ficar vazia.')
        return
    tarefas.append({'titulo': titulo,
                     'concluida': False})
    salvar_tarefas(tarefas)
    print('Tarefa adicionada!')

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    for i, tarefa in enumerate(tarefas, start=1):
        status = "[x]" if tarefa["concluida"] else "[ ]"
        print(f"{i}. {status} {tarefa['titulo']}")

def pedir_numero(tarefas, acao):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return None
    listar_tarefas(tarefas)
    try:
        numero = int(input(f"Número da tarefa para {acao}: "))
    except ValueError:
        print("Digite um número válido.")
        return None
    if numero < 1 or numero > len(tarefas):
        print("Esse número não existe.")
        return None
    return numero - 1

def concluir_tarefa(tarefas):
    indice = pedir_numero(tarefas, "concluir")
    if indice is None:
        return
    tarefas[indice]["concluida"] = True
    salvar_tarefas(tarefas)
    print("Tarefa concluída!")

def remover_tarefa(tarefas):
    indice = pedir_numero(tarefas, "remover")
    if indice is None:
        return
    removida = tarefas.pop(indice)
    salvar_tarefas(tarefas)
    print(f"Tarefa '{removida['titulo']}' removida.")


def pedir_numero(tarefas, acao):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return None
    listar_tarefas(tarefas)
    try:
        numero = int(input(f"Número da tarefa para {acao}: "))
    except ValueError:
        print("Digite um número válido.")
        return None
    if numero < 1 or numero > len(tarefas):
        print("Esse número não existe.")
        return None
    return numero - 1

def concluir_tarefa(tarefas):
    indice = pedir_numero(tarefas, "concluir")
    if indice is None:
        return
    tarefas[indice]["concluida"] = True
    salvar_tarefas(tarefas)
    print("Tarefa concluída!")

def remover_tarefa(tarefas):
    indice = pedir_numero(tarefas, "remover")
    if indice is None:
        return
    removida = tarefas.pop(indice)
    salvar_tarefas(tarefas)
    print(f"Tarefa '{removida['titulo']}' removida.")


def menu():
    tarefas = carregar_tarefas()
    while True:
        print("\n=== Gerenciador de Tarefas ===")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Concluir tarefa")
        print("4. Remover tarefa")
        print("0. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()