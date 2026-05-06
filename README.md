# 📦 Controle de Estoque - Livros e Empréstimos

Sistema completo de gerenciamento de estoque com **API REST** e **interface web interativa** desenvolvido em Python + Flask.

---

## ✅ Status do Projeto

| Item | Status |
|------|--------|
| Backend API | ✅ Funcional |
| Frontend Web | ✅ Implementado |
| Todos Endpoints | ✅ Testados |
| Bugs Corrigidos | ✅ Resolvidos |
| Dashboard | ✅ Operacional |
| Histórico | ✅ Funcional |

---

## 🚀 Como Iniciar

### 1️⃣ Instalar Dependências
```bash
pip install -r requirements.txt
```

### 2️⃣ Iniciar o Servidor
```bash
python app.py
```

### 3️⃣ Acessar a Aplicação
- **Interface Web**: http://localhost:5000
- **API REST**: http://localhost:5000 (todos os endpoints)

---

## 📋 Funcionalidades

### 📊 Dashboard
- Estatísticas de total de produtos e estoque
- Alertas de estoque baixo (< 5 unidades)
- Histórico das últimas 5 operações
- Atualização automática a cada 10 segundos

### 📦 Gerenciar Produtos
- ➕ Criar novos produtos
- 📋 Listar todos os produtos
- 🔄 Visualizar quantidade em tempo real
- ⚠️ Indicadores visuais de estoque crítico

### 📥 Registrar Entradas (Recebimento)
- Selecionar produto do estoque
- Informar quantidade recebida
- Registrar fornecedor
- Data automática ou manual
- ✅ Atualizar estoque automaticamente

### 📤 Registrar Saídas (Vendas)
- Selecionar produto do estoque
- Informar quantidade vendida
- Registrar cliente
- Data automática ou manual
- ✅ Validar estoque suficiente
- ⚠️ Impedir venda com estoque insuficiente
- 🔄 Atualizar estoque automaticamente

### 📋 Histórico Completo
- Visualizar todas as operações (Entrada e Saída)
- Ordenadas por data (mais recente primeiro)
- Detalhes de cada movimentação
- Rastreabilidade completa

---

## 🛠️ Arquitetura

### Estrutura de Diretórios
```
livros_e_emprestimos/
├── app.py                 # ⭐ Aplicação Flask principal
├── templates/
│   └── index.html        # 🎨 Frontend (HTML + CSS + JS)
├── routes/
│   └── routes.py         # 🔗 Endpoints da API
├── models/
│   ├── produto.py        # 📦 Modelo Produto
│   ├── entrada.py        # 📥 Modelo Entrada
│   └── saida.py          # 📤 Modelo Saída
├── requirements.txt      # 📚 Dependências Python
├── postman_collection.json # 🧪 Testes Postman
└── README.md            # 📖 Este arquivo
```

### Fluxo de Dados

```
┌─────────────┐
│  Frontend   │  (HTML + CSS + JavaScript)
│  (Browser)  │
└──────┬──────┘
       │ HTTP Requests/Responses
       ↓
┌─────────────────────┐
│  Flask App (app.py) │
│  + CORS Habilitado  │
└──────┬──────────────┘
       │
       ↓
┌──────────────────────┐
│  Routes (routes.py)  │  GET/POST
│  - /produtos         │
│  - /entradas         │
│  - /saidas           │
└──────┬───────────────┘
       │
       ↓
┌──────────────────────┐
│  Models              │
│  - Produto           │
│  - Entrada           │
│  - Saída             │
└──────┬───────────────┘
       │
       ↓
┌──────────────────────┐
│  Dados em Memória    │
│  (Listas Python)     │
│  - produtos[]        │
│  - entradas[]        │
│  - saidas[]          │
└──────────────────────┘
```

---

## 🔌 API REST - Documentação Completa

### Produtos

#### Listar Todos os Produtos
```http
GET /produtos
```
**Response 200:**
```json
[
  {
    "id": 1,
    "nome": "Notebook Dell",
    "quantidade": 15
  },
  {
    "id": 2,
    "nome": "Mouse Logitech",
    "quantidade": 25
  }
]
```

#### Criar Novo Produto
```http
POST /produtos
Content-Type: application/json

{
  "nome": "Monitor LG 27\"",
  "quantidade": 10
}
```
**Response 201:**
```json
{
  "id": 4,
  "nome": "Monitor LG 27\"",
  "quantidade": 10
}
```

---

### Entradas (Recebimento)

#### Listar Todas as Entradas
```http
GET /entradas
```
**Response 200:**
```json
[
  {
    "id": 1,
    "quantidade": 5,
    "data": "2026-05-05",
    "fornecedor": "Distribuidora X"
  }
]
```

#### Registrar Nova Entrada
```http
POST /entradas
Content-Type: application/json

{
  "id": 1,
  "quantidade": 5,
  "data": "2026-05-05",
  "fornecedor": "Distribuidora X"
}
```
**Response 201:**
```json
{
  "id": 1,
  "quantidade": 5,
  "data": "2026-05-05",
  "fornecedor": "Distribuidora X"
}
```

**Validações:**
- ❌ Produto não existe → 404
- ❌ Quantidade <= 0 → 400
- ❌ Data vazia → 400
- ❌ Fornecedor vazio → 400

---

### Saídas (Vendas/Distribuição)

#### Listar Todas as Saídas
```http
GET /saidas
```
**Response 200:**
```json
[
  {
    "id": 1,
    "quantidade": 3,
    "data": "2026-05-05",
    "cliente": "Cliente A"
  }
]
```

#### Registrar Nova Saída
```http
POST /saidas
Content-Type: application/json

{
  "id": 1,
  "quantidade": 3,
  "data": "2026-05-05",
  "cliente": "Cliente A"
}
```
**Response 201:**
```json
{
  "id": 1,
  "quantidade": 3,
  "data": "2026-05-05",
  "cliente": "Cliente A"
}
```

**Validações:**
- ❌ Produto não existe → 404
- ❌ Quantidade <= 0 → 400
- ❌ Estoque insuficiente → 400
- ❌ Data vazia → 400
- ❌ Cliente vazio → 400

---

## 🧪 Testes Realizados

### ✅ Testes Unitários

| Teste | Resultado |
|-------|-----------|
| Criar produto com valores válidos | ✅ Sucesso |
| Criar entrada válida | ✅ Sucesso |
| Criar saída válida | ✅ Sucesso |
| Atualizar estoque em entrada | ✅ +5 unidades |
| Atualizar estoque em saída | ✅ -3 unidades |
| Rejeitar saída sem estoque | ✅ Erro 400 |
| Listar produtos | ✅ 4 produtos |
| Listar entradas | ✅ 1 entrada |
| Listar saídas | ✅ 1 saída |

### 🚀 Testes via Postman

Arquivo: `postman_collection.json`

Contém 9 requisições de teste cobrindo todos os endpoints.

---

## 🔧 Bugs Corrigidos

### 🐛 Bug #1: Retorno vazio em `remover_estoque()`
**Problema:** Método não retornava nada quando bem-sucedido, causando lógica quebrada.
**Solução:** Adicionado retorno `"Sucesso"` para sucesso e `"Quantidade insuficiente"` para erro.

```python
def remover_estoque(self, quantidade):
    if quantidade > self.quantidade:
        return "Quantidade insuficiente"
    self.quantidade -= quantidade
    return "Sucesso"  # ✅ Adicionado
```

### 🐛 Bug #2: Geração ineficiente de IDs
**Problema:** `len(produtos) + 1` não funciona corretamente se produtos forem removidos.
**Solução:** Usar `max([p.id for p in produtos], default=0) + 1`.

```python
novo_id = max([p.id for p in produtos], default=0) + 1  # ✅ Robusto
```

### 🐛 Bug #3: CORS não habilitado
**Problema:** Frontend não conseguia fazer requisições à API.
**Solução:** Adicionar `flask-cors` e habilitar em `app.py`.

```python
from flask_cors import CORS
CORS(app)  # ✅ Habilitado
```

---

## 📊 Dados Iniciais

A aplicação começa com 3 produtos pré-cadastrados:

| ID | Produto | Quantidade |
|----|---------|-----------|
| 1 | Notebook Dell | 10 |
| 2 | Mouse Logitech | 25 |
| 3 | Teclado Mecânico | 8 |

**Total em Estoque:** 43 unidades

---

## 📱 Interface Web

### Design
- 🎨 **Tema Moderno**: Gradiente azul com cards interativos
- 📱 **Responsivo**: Funciona em desktop, tablet e mobile
- 🚀 **Rápido**: Recarregamento automático a cada 10 segundos
- ♿ **Acessível**: Navegação clara e intuitiva

### Componentes
- **Header**: Título e descrição da aplicação
- **Tabs**: Navegação entre seções
- **Forms**: Entrada de dados validada
- **Cards**: Exibição de dados em grade
- **Alerts**: Notificações de sucesso/erro
- **Stats**: Números-chave do sistema

### Cores
- **Primária**: `#6366f1` (Índigo)
- **Sucesso**: `#10b981` (Verde)
- **Perigo**: `#ef4444` (Vermelho)
- **Aviso**: `#f59e0b` (Âmbar)

---

## 💾 Dados em Memória

⚠️ **Importante:** Todos os dados são armazenados em listas Python na memória RAM.

```python
# Em routes.py
produtos = []      # Começam com 3 produtos
entradas = []      # Vazio inicialmente
saidas = []        # Vazio inicialmente
```

**Implicações:**
- ✅ Muito rápido (sem I/O de disco)
- ✅ Simples para desenvolvimento
- ❌ Perdido ao reiniciar servidor
- ❌ Não é adequado para produção

### Para Produção
Integrar com banco de dados:
- PostgreSQL
- MySQL
- MongoDB
- SQLite (com arquivo persistido)

---

## 👥 Equipe e Responsabilidades

| Dev | Responsabilidade | Status |
|-----|-----------------|--------|
| **Erick** | Lógica + Integração + Testes + Frontend | ✅ Completo |
| **Caio** | Endpoints da API | ✅ Completo |
| **Vinicius** | Lógica de Estoque | ✅ Completo |
| **Mari** | Documentação e Contratos | ✅ Completo |
| **Marcos** | Regras de Negócio | ✅ Completo |

---

## 🎯 Próximos Passos (Futuro)

- [ ] 💾 Persistência em banco de dados SQL
- [ ] 🔐 Sistema de autenticação e autorização
- [ ] 📊 Relatórios e gráficos
- [ ] 📄 Exportação para PDF/Excel
- [ ] 📧 Alertas por email
- [ ] 📱 Aplicativo mobile
- [ ] 🔔 Notificações em tempo real
- [ ] 🔄 Backup automático

---

## 🧰 Tecnologias Utilizadas

### Backend
- **Python 3.13.13** - Linguagem
- **Flask 2.3.3** - Framework web
- **Werkzeug 2.3.7** - WSGI utilities
- **flask-cors 4.0.0** - CORS support

### Frontend
- **HTML5** - Estrutura
- **CSS3** - Estilização (Flexbox, Grid, Gradientes)
- **JavaScript (Vanilla)** - Interatividade
- **Fetch API** - Requisições HTTP

### Ferramentas
- **Git** - Controle de versão
- **VS Code** - Editor
- **Postman** - Testes de API
- **PowerShell** - Terminal

---

## 📦 Dependências

Ver arquivo `requirements.txt`:
```
Flask==2.3.3
Werkzeug==2.3.7
flask-cors==4.0.0
```

Instalar com:
```bash
pip install -r requirements.txt
```

---

## 📖 Documentação Adicional

- 📋 [Contrato do Projeto](docs/contrato.md)
- 📏 [Regras de Negócio](docs/regras.md)
- 👤 [Tarefas por Desenvolvedor](docs/)

---

## 🧪 Como Testar

### Via Postman
1. Abra Postman
2. Importe `postman_collection.json`
3. Configure a variável `baseUrl` para `http://127.0.0.1:5000`
4. Execute os 9 testes na sequência

### Via Frontend
1. Abra http://localhost:5000
2. Navegue pelas abas
3. Teste criar produtos, entradas e saídas
4. Verifique o histórico

### Via Terminal
```bash
# Testar GET /produtos
curl http://localhost:5000/produtos

# Testar POST /produtos
curl -X POST http://localhost:5000/produtos \
  -H "Content-Type: application/json" \
  -d '{"nome":"Novo Produto","quantidade":10}'
```

---

## 🐛 Troubleshooting

### Erro: `ModuleNotFoundError: No module named 'flask'`
```bash
pip install Flask==2.3.3
```

### Erro: `ModuleNotFoundError: No module named 'flask_cors'`
```bash
pip install flask-cors==4.0.0
```

### Porta 5000 já está em uso
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac
lsof -i :5000
kill -9 <PID>
```

### Servidor não responde
- Verificar se está rodando: `http://localhost:5000`
- Verificar logs no terminal
- Reiniciar: Ctrl+C e rodar novamente

---

## 📝 Licença

Projeto educacional - Livre para uso em estudos e desenvolvimento.

---

## 📞 Contato

Para dúvidas ou sugestões, abra uma issue ou entre em contato com a equipe de desenvolvimento.

---

**Versão:** 1.0.0  
**Data:** 05 de Maio de 2026  
**Status:** ✅ Produção
