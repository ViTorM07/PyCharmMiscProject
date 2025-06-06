from exercicio115.lib.arquivo import*
from exercicio115.lib.interface import*
from time import sleep

# cabecalho('Testando 123')
# cabecalho('SISTEMA ARQUIVO v1.0')

arq = 'cursoemvideo.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
    pass
else:
    print('Arquivo nao encontrado!')
    criarArquivo(arq)
while True:
    resposta = menu(['Criar aquivo', 'Cadastrar pessoas', 'Listar Pessoas', 'Sair do Sistema'])
    if resposta ==1:
        #opcao de listar o conteudo de um arquivo
        # cabecalho('Opcao 1')
        lerArquivo(arq)
    elif(resposta ==2):
        #Opcao para cadastrar um pessoa nova
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif(resposta ==3):
        #Opcao para sair do sistema
        cabecalho('Saindo do sistema, até logo...')
        break
    else:
        print('\033[31mErro! Digite umq opcao válida!\033[m')
    sleep(2)