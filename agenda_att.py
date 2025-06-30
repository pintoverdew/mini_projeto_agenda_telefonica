agenda = []  # Lista que armazenará os contatos como listas de campos (nome, sobrenome, telefone, etc.)

# Funções de entrada com validação para cada campo do contato

def perguntar_nome():
    while True:
        nome = input("Nome (até 20 letras, pode conter espaços): ").strip()
        # Remove espaços extras no início/fim e verifica se os caracteres são letras ou espaços
        if(len(nome) <= 20 and len(nome) >= 1 and all(c.isalpha() or c == " " for c in nome)):
            return nome
        else:
            print("O valor não atende a especificação do campo.")

def perguntar_sobrenome():
    while True:
        sobrenome = input("Sobrenome (até 20 letras, pode conter espaços): ").strip()
        # Remove espaços extras no início/fim e verifica se os caracteres são letras ou espaços
        if (len(sobrenome) <= 20 and len(sobrenome) >= 1 and all(c.isalpha() or c == " " for c in sobrenome)):
            return sobrenome
        else:
            print("O valor não atende a especificação do campo.")

def perguntar_telefone():
    while True:
        telefone = input("Telefone (até 15 números): ").strip()
        if telefone == "" or (telefone.isdigit() and len(telefone) <= 15):
            return telefone
        else:
            print("O valor não atende a especificação do campo.")

def perguntar_celular():
    while True:
        celular = input("Celular (até 15 números): ").strip()
        if (celular.isdigit() and len(celular) <= 15 and len(celular) >= 1):
            return celular
        else:
            print("O valor não atende a especificação do campo.")

def perguntar_email():
    while True:
        email = input("Email (formato nome@dominio.ext): ").strip()
        if email == "":
            return email
        if "@" in email and "." in email:
            partes = email.split("@")
            if len(partes) == 2 and partes[0] != "" and partes[1] != "":
                dominio = partes[1].split(".")
                if len(dominio) == 2 and dominio[0] != "" and dominio[1] != "":
                    return email
        print("O valor não atende a especificação do campo.")

def perguntar_mes():
    while True:
        mes = input("Mês de aniversário (01 a 12): ").strip()
        if mes.isdigit() and len(mes) == 2 and 1 <= int(mes) <= 12:
            return mes
        else:
            print("O valor não atende a especificação do campo.")

def perguntar_dia():
    while True:
        dia = input("Dia de aniversário (01 a 31): ").strip()
        if dia.isdigit() and len(dia) == 2 and 1 <= int(dia) <= 31:
            return dia
        else:
            print("O valor não atende a especificação do campo.")

def perguntar_ano():
    while True:
        ano = input("Ano de aniversário (1900 a 2025): ").strip()
        if ano.isdigit() and len(ano) == 4 and 1900 <= int(ano) <= 2025:
            return ano
        else:
            print("O valor não atende a especificação do campo.")

# Função para inserir novo contato na agenda

def insere_contato():
    if len(agenda) >= 5:
        print("Não existe mais espaço na agenda.")
        return

    nome = perguntar_nome()
    sobrenome = perguntar_sobrenome()
    telefone = perguntar_telefone()
    celular = perguntar_celular()
    email = perguntar_email()
    mes = perguntar_mes()
    dia = perguntar_dia()
    ano = perguntar_ano()

    contato = [nome, sobrenome, telefone, celular, email, mes, dia, ano]
    agenda.append(contato)
    print(f"O contato {nome} {sobrenome} foi inserido com sucesso.")

# Função para listar contatos

def lista_contatos():
    for i, c in enumerate(agenda):
        print(f"{i+1} - {c[0]} {c[1]}")

# Função para buscar contato por nome e sobrenome

def busca_contato():
    nome = input("Digite o nome: ").strip()
    sobrenome = input("Digite o sobrenome: ").strip()
    for c in agenda:
        if c[0].lower() == nome.lower() and c[1].lower() == sobrenome.lower():
            print(f"1 - {c[0]} {c[1]}\n2 - {c[2]}\n3 - {c[3]}\n4 - {c[4]}\n5 - {c[6]}/{c[5]}/{c[7]}")
            return
    print("Contato não encontrado.")

# Função para atualizar um contato

def atualiza_contato():
    nome = input("Digite o nome do contato: ").strip()
    sobrenome = input("Digite o sobrenome do contato: ").strip()
    for c in agenda:
        if c[0].lower() == nome.lower() and c[1].lower() == sobrenome.lower():
            while True:
                print("""
1 - Nome
2 - Sobrenome
3 - Telefone
4 - Celular
5 - Email
6 - Mês de Aniversário
7 - Dia de Aniversário
8 - Ano de Aniversário
9 - Voltar ao menu
""")
                opcao = input("Escolha o campo a atualizar: ").strip()
                if opcao == "1":
                    c[0] = perguntar_nome()
                elif opcao == "2":
                    c[1] = perguntar_sobrenome()
                elif opcao == "3":
                    c[2] = perguntar_telefone()
                elif opcao == "4":
                    c[3] = perguntar_celular()
                elif opcao == "5":
                    c[4] = perguntar_email()
                elif opcao == "6":
                    c[5] = perguntar_mes()
                elif opcao == "7":
                    c[6] = perguntar_dia()
                elif opcao == "8":
                    c[7] = perguntar_ano()
                elif opcao == "9":
                    break
                else:
                    print("Campo inválido. Escolha novamente.")
                    continue
                print("Campo atualizado com sucesso.")
            return
    print("Contato não encontrado.")

# Função para remover um contato

def remove_contato():
    nome = input("Digite o nome do contato a remover: ").strip()
    sobrenome = input("Digite o sobrenome: ").strip()
    for i, c in enumerate(agenda):
        if c[0].lower() == nome.lower() and c[1].lower() == sobrenome.lower():
            del agenda[i]
            print(f"O contato {nome} {sobrenome} foi excluído com sucesso.")
            return
    print("Contato não encontrado.")

# Menu principal que executa o programa

def menu():
    while True:
        print("""
1 - Inserir Contato
2 - Listar Contatos
3 - Buscar Contato
4 - Atualizar Contato
5 - Remover Contato
6 - Sair
""")
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            insere_contato()
        elif escolha == "2":
            lista_contatos()
        elif escolha == "3":
            busca_contato()
        elif escolha == "4":
            atualiza_contato()
        elif escolha == "5":
            remove_contato()
        elif escolha == "6":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Inicia o programa executando o menu
menu()
