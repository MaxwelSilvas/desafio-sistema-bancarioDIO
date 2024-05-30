# Desafio DIO Sistema Bancário

Este repositório contém a solução para o desafio proposto pela [Digital Innovation One (DIO)](https://www.dio.me) durante o Bootcamp Python AI Backend Developer, onde o objetivo é desenvolver um simples sistema bancário utilizando a linguagem de programação Python.

## Descrição do Desafio

O desafio consiste em implementar um sistema bancário com as seguintes funcionalidades:

1. **Depósito**: Permite ao usuário adicionar um valor ao saldo bancário.
2. **Saque**: Permite ao usuário retirar um valor do saldo bancário, respeitando o limite de saques diários e o limite de valor por saque.
3. **Extrato**: Exibe todas as transações realizadas (depósitos e saques) e o saldo atual.
4. **Sair**: Encerra o sistema bancário.

## Funcionalidades

### Depósito

- O usuário pode realizar depósitos de qualquer valor positivo.
- O valor depositado é adicionado ao saldo bancário.
- Cada depósito é registrado para fins de extrato.

### Saque

- O usuário pode realizar saques, respeitando as seguintes condições:
  - O valor do saque deve ser positivo.
  - O valor do saque não pode exceder o saldo disponível.
  - O valor máximo por saque é de R$ 500,00.
  - O usuário tem um limite de 3 saques diários.
- Cada saque realizado é registrado para fins de extrato.

### Extrato

- Exibe todas as transações realizadas (depósitos e saques) e o saldo atual.

# Possui outra Branch com a versão atualizada
