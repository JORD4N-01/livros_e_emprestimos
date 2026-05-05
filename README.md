# � Controle de Estoque API

Uma API REST simples para gerenciamento de produtos, entradas e saídas desenvolvida com Python e Flask.

## 🎯 Objetivo

Sistema simples e funcional para controlar o estoque de produtos, registrando entradas (compras/recebimentos) e saídas (vendas/retiradas), com foco em organização e rastreabilidade.

## 🛠️ Stack Tecnológico

- **Python** - Linguagem principal
- **Flask** - Framework web
- **JSON** - Formato de dados para requisições e respostas
- **Mockdata** - Dados armazenados em memória (hardcoded), sem integração com banco de dados

## 📁 Estrutura do Projeto

```
controle_estoque/
├── app.py              # Aplicação principal
├── models/             # Classes de dados
│   ├── produto.py      # Classe Produto
│   ├── entrada.py      # Classe Entrada
│   └── saida.py        # Classe Saida
├── routes/             # Endpoints da API
│   └── routes.py       # Definição das rotas
├── docs/               # Documentação do projeto
├── requirements.txt    # Dependências do projeto
└── README.md          # Este arquivo
```


## ℹ️ Observação Importante

Este projeto **NÃO utiliza banco de dados**. Todos os dados são armazenados em listas em memória (mockdata/hardcoded) apenas para fins de simulação e testes.

Ao reiniciar a aplicação, todos os dados voltam ao estado inicial.

---
## 🚀 Como Usar

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone este repositório:
```bash
git clone https://github.com/JORD4N-01/controle_estoque
cd controle_estoque
```

2. Instale as dependências:
```bash
pip install -r requeriments.txt
```

3. Execute a aplicação:
```bash
python app.py
```

A API estará disponível em `http://localhost:5000`

## 📡 Endpoints da API

### Produtos

- `GET /produtos` - Lista todos os produtos
- `POST /produtos` - Cadastra um novo produto

### Entradas (Entrada de Estoque)

- `GET /entradas` - Lista todas as entradas
- `POST /entradas` - Registra uma nova entrada de produto

### Saídas (Saída de Estoque)

- `GET /saidas` - Lista todas as saídas
- `POST /saidas` - Registra uma nova saída de produto

## 🧪 Testes

Recomendamos usar o **Postman** para testar os endpoints:

1. Importe a coleção de testes (se disponível)
2. Configure as requisições para `http://localhost:5000`
3. Teste todos os endpoints para garantir funcionamento

## 📝 Exemplos de Uso

### Cadastrar um Produto

```json
POST /produtos
Content-Type: application/json

{
    "nome": "Notebook Dell",
    "quantidade": 10
}
```

### Registrar Entrada de Estoque

```json
POST /entradas
Content-Type: application/json

{
    "id": 1,
    "quantidade": 20,
    "data": "2024-01-15",
    "fornecedor": "Distribuidora Tech"
}
```

### Registrar Saída de Estoque

```json
POST /saidas
Content-Type: application/json

{
    "id": 1,
    "quantidade": 5,
    "data": "2024-01-16",
    "cliente": "Empresa ABC"
}
```

## 🔧 Desenvolvimento

### Padrões do Projeto

- Código em português (classes e endpoints)
- Estrutura obrigatória de diretórios
- Commits organizados
- Testes obrigatórios antes de finalizar

### Equipe

- **MARI** → Models (classes Produto, Entrada e Saida)
- **MARCOS** → Routes (endpoints da API)
- **ERICK** → Lógica + Integração + Testes
- **Jordan** → Integração final + organização

## 📋 Regras Importantes

- ❌ Não modificar `app.py` sem autorização
- ❌ Não criar arquivos fora da estrutura definida
- ❌ Não mudar nomes de classes ou rotas sem avisar
- ❌ Não subir código quebrado

## 🏆 Objetivo Final

Sistema simples, funcionando e bem organizado.

> "Melhor um sistema simples funcionando do que algo complexo quebrado."

## 📄 Licença

Este projeto está sob licença MIT.