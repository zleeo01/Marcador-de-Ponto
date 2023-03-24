import datetime

# CAMINHO ONDE ESTA O TXT (REGISTRO)
caminho_do_arquivo = "C:\\Users\\Usuario\\Desktop\\TRABALHO\\PONTO\\registro_de_ponto.txt"

# PEDIR O NOME DO FUCIONARIO
nome_funcionario = input("Por favor, informe o seu nome: ")

# PUXAR A DATA AUTOMATICO DO PC
agora = datetime.datetime.now()

# FORMATAR DATA E HORA
data_atual = agora.strftime("%d/%m/%Y")
hora_atual = agora.strftime("%H:%M:%S")

# NOVO REGISTRO DO PONTO
with    open(caminho_do_arquivo, "a") as arquivo:
    #PEDIR SE É ENTRADA OU SAIDA
    entrada_saida = input("Você está fazendo uma ENTRADA ou SAÍDA? ")
    #
    arquivo.write(f"{nome_funcionario} fez {entrada_saida} em {data_atual} às {hora_atual}\n")

    # Imprimir uma mensagem de confirmação para o usuário (APENAS NO VSCODE)
    print(f"Registro de ponto {entrada_saida} efetuado com sucesso em {data_atual} às {hora_atual}.")

# Mostrar mensagem de conclusão ao usuário (APENAS NO VSCODE)
print("Ponto registrado com sucesso!")
