# 📜 Contrato de Desenvolvimento — Controle de Estoque API

## 🤖 Regra de Uso de IA (OBRIGATÓRIO)

Ao gerar código com IA, SEMPRE:

1. Informar explicitamente este contrato como contexto
2. Pedir para seguir estritamente:
   - nomes de campos
   - estrutura JSON
   - endpoints definidos
3. Não permitir que a IA crie:
   - novos campos
   - novos nomes de atributos
   - novas rotas fora do padrão

4. Se houver conflito entre resposta da IA e este contrato:
   👉 O CONTRATO SEMPRE VENCE

## 🎯 Objetivo
Garantir que todos os desenvolvedores (e ferramentas de IA) sigam o mesmo padrão, evitando inconsistências e problemas de integração.

---

## 🧠 Padrão Geral

- Linguagem: Python
- Framework: Flask
- Comunicação: JSON
- Projeto simples (sem banco de dados)
- Armazenamento em memória (listas mockadas/hardcoded, sem persistência)

---

## 📦 Estrutura de Dados (OBRIGATÓRIA)

### � Produto

```json
{
  "id": 1,
  "nome": "Notebook Dell",
  "quantidade": 10
}
```

### 📥 Entrada (Entrada de Estoque)

```json
{
  "id": 1,
  "quantidade": 20,
  "data": "2024-01-15",
  "fornecedor": "Distribuidora Tech"
}
```

### � Saída (Saída de Estoque)

```json
{
  "id": 1,
  "quantidade": 5,
  "data": "2024-01-16",
  "cliente": "Empresa ABC"
}
---