from Pessoa import Pessoa
class Professor(Pessoa):

    def __init__(self, nome, documento, matricula):
        self.nome = nome
        self.documento = documento
        self.matricula = matricula