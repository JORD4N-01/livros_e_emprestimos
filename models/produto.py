class Produto:
    def __init__(self, id, nome, quantidade):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "quantidade": self.quantidade,
        }

    def adicionar_estoque(self, quantidade):
        self.quantidade += quantidade

    def remover_estoque(self, quantidade):
        if quantidade > self.quantidade:
            return "Quantidade insuficiente"
        self.quantidade -= quantidade