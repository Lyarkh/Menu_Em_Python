from .template_opcao import TemplateOpcao

class Opcao01(TemplateOpcao):

    def __str__(self):
        return 'opcao_1'
    
    def __eq__(self, outro):
        return type(self) == type(outro)
    
    def run(self):
        print('esta funcionando a opção 01')
        input('presione qualquer tecla para voltar para o menu')
    
    def muda_estado(self):
        return 1

class Opcao02(TemplateOpcao):

    def __str__(self):
        return 'opcao_2'
    
    def run(self):
        print('esta funcionando a opção 02')
        input('presione qualquer tecla para voltar para o menu')
    
    def muda_estado(self):
        return 1

class Opcao03(TemplateOpcao):

    def __str__(self):
        return 'opcao_3'
    
    def run(self):
        print('esta funcionando a opção 03')
        input('presione qualquer tecla para voltar para o menu')
    
    def muda_estado(self):
        return 1

class Opcao04(TemplateOpcao):

    def __str__(self):
        return 'opcao_4'
    
    def run(self):
        print('esta funcionando a opção 04')
        input('presione qualquer tecla para voltar para o menu')
    
    def muda_estado(self):
        return 1

class Opcao05(TemplateOpcao):

    def __str__(self):
        return 'opcao_5'
    
    def run(self):
        print('esta funcionando a opção 05')
        input('presione qualquer tecla para voltar para o menu')
    
    def muda_estado(self):
        return 1

class Opcao06(TemplateOpcao):

    def __str__(self):
        return 'opcao_6'
    
    def run(self):
        print('esta funcionando a opção 06')
        input('presione qualquer tecla para voltar para o menu')
    
    def muda_estado(self):
        return 1

