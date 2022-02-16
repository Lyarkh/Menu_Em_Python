from template_opcao import TemplateOpcao

class TodasOpcoes:
    def __init__(self):
        self.opcoes = [Opcao01(), Opcao02(), Opcao03(), Opcao04()]


class Opcao01(TemplateOpcao):

    def __str__(self):
        return 'opcao_01'
    
    def run(self):
        print('esta funcionando a opção 01')

class Opcao02(TemplateOpcao):

    def __str__(self):
        return 'opcao_01'
    
    def run(self):
        print('esta funcionando a opção 02')

class Opcao03(TemplateOpcao):

    def __str__(self):
        return 'opcao_01'
    
    def run(self):
        print('esta funcionando a opção 03')

class Opcao04(TemplateOpcao):

    def __str__(self):
        return 'opcao_01'
    
    def run(self):
        print('esta funcionando a opção 04')