class Saida:
    def __init__(self, id, quantidade, data, cliente):
        self.id = id
        self.quantidade = quantidade
        self.data = data
        self.cliente = cliente

    def to_dict(self):
        return {
            "id": self.id,
            "quantidade": self.quantidade,
            "data": self.data,
            "cliente": self.cliente,
        }