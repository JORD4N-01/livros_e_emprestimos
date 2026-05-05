# 🧩 Tarefa — MARI (Modelagem com POO)

## 🎯 Objetivo
Criar as classes do sistema que representam os dados do controle de estoque.

Você será responsável por estruturar os objetos principais do sistema utilizando Programação Orientada a Objetos (POO).

---

# 📦 Classes que devem ser criadas

Você deve criar 3 classes:

- Produto
- Entrada
- Saida

Cada classe representa uma parte do sistema.

---

# 🧠 O que você precisa implementar

## 📌 1. Método construtor (`__init__`)

### O que fazer:
Criar o método que inicializa os dados da classe.

### Por quê:
Sem esse método, não conseguimos criar objetos com informações definidas.

### Exemplo conceitual:
> Quando criamos um produto, precisamos definir id, nome e quantidade.

---

## 📌 2. Método de conversão (`to_dict`)

### O que fazer:
Criar um método que transforme o objeto em um formato de dicionário.

### Por quê:
A API trabalha com JSON, então precisamos converter os objetos para esse formato.

### Importante:
- Retornar um dicionário com os atributos da classe
- Os nomes devem seguir o padrão do projeto

---

## 📌 3. Métodos de comportamento (somente para Produto)

### 📥 Entrada de estoque

#### O que fazer:
Criar um método que aumente a quantidade do produto.

#### Por quê:
Quando um produto entra no estoque, sua quantidade deve ser atualizada.

---

### 📤 Saída de estoque

#### O que fazer:
Criar um método que diminua a quantidade do produto.

#### Por quê:
Quando um produto sai do estoque, precisamos reduzir a quantidade.

---

### ⚠️ Validação (importante)

#### O que fazer:
Garantir que não seja possível remover mais produtos do que existe.

#### Por quê:
Evita erros e mantém o sistema consistente.

---

# 📚 Estrutura esperada das classes

## Produto
Deve conter:
- id
- nome
- quantidade

Deve possuir:
- construtor
- método de conversão (to_dict)
- método de adicionar estoque
- método de remover estoque

---

## Entrada
Deve conter:
- id
- quantidade
- data
- fornecedor

Deve possuir:
- construtor
- método de conversão (to_dict)

---

## Saida
Deve conter:
- id
- quantidade
- data
- cliente

Deve possuir:
- construtor
- método de conversão (to_dict)

---

# ⚠️ Regras importantes

- Não inventar atributos novos
- Seguir exatamente os nomes definidos
- Não adicionar funcionalidades fora do escopo
- Manter o código simples

---

# 🏆 Dica

> Pense nas classes como “representações do mundo real”.

Produto → algo no estoque  
Entrada → algo chegando  
Saída → algo saindo  

---

# 🎯 Objetivo final

Quando terminar, você deve conseguir:

- Criar objetos corretamente
- Representar os dados do sistema
- Preparar os dados para serem usados pela API

---

# 👑 Observação final

Se tiver dúvida:
- volte para o contrato.md
- ou pergunte antes de mudar algo

👉 Isso evita retrabalho para todo o grupo