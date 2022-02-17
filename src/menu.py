import os
from time import sleep

from classes.opcoes import Opcao01, Opcao02, Opcao03, Opcao04, Opcao05, Opcao06
from classes.encerramento import Encerramento

class Menu:
    def __init__(self):
        self.estado = 1 

    def run(self):
        self.apresenta_programa()
        sleep(0.8)
        
        while self.estado:
            self.limpa_tela()
            self.imprime_menu()
            self.escolha_opcao()

    def verificando_estado(self, estado)-> bool:
        self.estado = estado.muda_estado()
    
        return self.estado

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
        lista_opcoes = [Opcao01(), Opcao02(), Opcao03(),
                        Opcao04(), Opcao05(), Opcao06(), Encerramento()]

        print('Qual opção deseja?')
        opcao_inserida = int(input('-> ').strip())
        self.tratamento_opcao(opcao_inserida)
        
        for id, _ in enumerate(lista_opcoes):
            if opcao_inserida == id+1:
                lista_opcoes[id].run()
                self.estado = self.verificando_estado(lista_opcoes[id])
    
    def tratamento_opcao(self, opcao):
        opcoes_aceitas = [1,2,3,4,5,6,7]

        if not opcao in opcoes_aceitas:
            print('--Digite uma opção válida--')
            print('São aceitas opções de 1 a 7')
            

if __name__ == '__main__':
    menu = Menu().run()