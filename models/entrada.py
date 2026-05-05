class Entrada:
    def __init__(self, id, quantidade, data, fornecedor):
        self.id = id
        self.quantidade = quantidade
        self.data = data
        self.fornecedor = fornecedor

    def to_dict(self):
        return {
            "id": self.id,
            "quantidade": self.quantidade,
            "data": self.data,
            "fornecedor": self.fornecedor,
        }