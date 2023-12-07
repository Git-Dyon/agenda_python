def menu():
    voltar_menu_principal = 's'
    while voltar_menu_principal == 's':
        opcao = input('''
        =================================================================
                            PROJETO AGENDA EM PYTHON
        
        [1] PARA CADASTRAR CONTATO
        [2] PARA LISTAR CONTATO
        [3] DELETAR CONTATO
        [4] BUSCAR CONTATO PELO ID
        [5] SAIR
        =================================================================
        ESCOLHA UMA DAS OPOÇÕES A CIMA: 
        ''')
        # >>>>>>>>>>>>>>>>>> Criando o menu de opções <<<<<<<<<<<<<<<<
        if opcao == '1':
            cadastrar_contato()
        elif opcao == '2':
            listar_contato()
        elif opcao == '3':
            deletar_contato()
        elif opcao == '4':
            buscar_contato()
        else:
            sair()
        voltar_menu_principal = input('Deseja voltar ao menu principal? S/N: ').lower()
            
# >>>>>>>>>>>>>> Definindo as funções de cada opção <<<<<<<<<<
def cadastrar_contato():
    idcontato = input('Escolha o ID do seu contato sendo de 0 a 99: ')
    name = input('Escreva o nome do seu contato: ')
    phone = input('Escreva o telefone do contato: ')
    email = input('Digite o e-mail: ')
    try:
        agenda = open('agenda.txt', 'a')
        dados = f'{idcontato};{name};{phone};{email}\n'
        agenda.write(dados)
        agenda.close()
        print('Contato armazenado com SUCESSO!')
    except:
        print('Erro na gravação do contato')

def listar_contato():
    agenda = open('agenda.txt', 'r')
    for contato in agenda:
        print(contato)
    agenda.close()

def deletar_contato():
    nome_deletado = input('Digite o nome a ser deletado: ').lower()
    agenda = open('agenda.txt', 'r')
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nome_deletado not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open('agenda.txt', 'w')
    for i in aux2:
        agenda.write(i)
    print('Contato deletado com sucesso')
    listar_contato()

def buscar_contato():
    nome = input('Digite o ID a ser procurado: ')
    with open('agenda.txt', 'r') as agenda:
        for contato in agenda:
            if nome in contato.split(';')[0]:
                print(contato)

def sair():
    print('ATÉ MAIS!!!')
    exit()

def main():
    menu()

main()
