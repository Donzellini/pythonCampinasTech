class Veiculo:
    """
    Classe que define o veículo
    """
    def andar(self):
        """
        Andar
        """
        print("O veículo está andando...")


class Veiculo_Terrestre(Veiculo):
    """
    Classe que define o veículo Terrestre
    """
    def andar(self):
        """
        Andar
        """
        print("O Veículo Terrestre está andando...")


class Carro(Veiculo_Terrestre):
    """
    Classe que define o carro
    """
    def andar(self):
        """
        Andar o carro
        """
        print("O carro está andando...")
    
c = Carro()
c.andar()
