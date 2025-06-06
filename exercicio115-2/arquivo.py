with open ('dados.txt', 'a') as arquivo:

    nome = input('Digite seu nome: ')
    idade = input('Digite sua idade: ')
    email = input('Digite seu email: ')

    linha = (f"Nome: {nome}|Idade: {idade}|Email:{email}\n")
    arquivo.write(linha)

    print('Dados salvos com sucesso!')