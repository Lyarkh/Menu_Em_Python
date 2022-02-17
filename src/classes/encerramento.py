from .template_opcao import TemplateOpcao

class Encerramento(TemplateOpcao):

    def __str__(self):
        return 'opcao 07 - opcao_de_encerramento'
    
    def run(self):
        print('esta funcionando a opção 07')
        input('presione qualquer tecla para continuar')
    
    def muda_estado(self):
        #utilizado para mudar o estado do menu e encerrar o programa.
        print('-----------------------')
        print('Encerrando o programa!!')
        print(' ---até a próxima---!  ')

        return 0
