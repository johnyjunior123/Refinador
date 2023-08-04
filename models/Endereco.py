class Endereco:

    def __init__(self, tipo, logradouro, bairro, cidade, estado, geolocalizacao):
        self.tipo = tipo
        self.logradouro = logradouro
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.latlong = geolocalizacao

    def __str__(self):
        return f" Tipo: {self.tipo} | Logradouro: {self.logradouro} | Bairro: {self.bairro} | Cidade: {self.cidade} | Estado: {self.estado} | Point: {self.geolocalizacao}"