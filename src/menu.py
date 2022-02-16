import os
from time import sleep

class Menu:
            
    def run(self):
        self.apresenta_programa()
        
        self.limpa_tela()
        self.imprime_menu()
        self.escolha_opcao()

    def apresenta_programa(self):
        print('Iniciando...')
        sleep(0.8)
        self.limpa_tela()
        print('----------------------  ') 
        print('-----Bem vindo!!------  ')
        print('----------------------\n')  
                  

    def imprime_menu(self):
        print('----------------------')
        print('---------Menu!!-------')
        print('----------------------')
        print('(1)     Opção 01      ')
        print('(2)     Opção 02      ')
        print('(3)     Opção 03      ')
        print('(4)     Opção 04      ')
        print('(5)     Opção 05      ')
        print('(6)     Opção 06      ')
        print('(7) Sair do programa\n')
    
    def limpa_tela(self):
        os.system('cls')

    def escolha_opcao(self):
        # verificar e arrumar esta parte
        # transformar as opções em classes
        # criar lista com todas as opções disponíveis
        # criar metodo __str__ para cada opção para ver se funciona do jeito que está querendo

        opcao_teste = self.opcao_1
        
        print('Qual opção deseja?')

        opcao = input('-> ')
        opcao_completa = f'self.opcao_{opcao}'

        print (str(opcao_teste))
        print(opcao_completa)

        if opcao_completa == str(opcao_teste):
            self.opcao_1()
        else:
            print('deu errado')

    def opcao_1(self):
        print('deu certo o teste que você esta fazendo')
        pass

    def opcao_2(self):
        pass

    def opcao_3(self):
        pass

    def opcao_4(self):
        pass

    def opcao_5(self):
        pass

    def opcao_6(self):
        pass

    def opcao_7(self):
        pass

if __name__ == '__main__':
    menu = Menu()
    menu.run()