# Controle de Hospedagem Jf

Sistema de gerenciamento de hospedagem de um hotel, desenvolvido em **Python** para a disciplina **Orientação a Objetos** do **Prof. Henrique Moura** (UnB).

O projeto evolui em quatro níveis. Cada nível entregue é marcado por um commit próprio, e o histórico do repositório mostra o sistema crescendo de um nível para o outro.

## Finalidade

Simular a rotina de um hotel: cadastro de clientes e funcionários, controle de quartos, registro de hospedagens (check-in e check-out) e lançamento de gastos dos hóspedes.

O projeto aplica herança, polimorfismo, composição, associação e dependência, com modelagem em UML no padrão **ECB** (Entity, Control, Boundary).

## Níveis do projeto

| Nível | Propósito | Interface | Vídeo         | Commit de entrega    | Status |
|:---:|---|---|---------------|----------------------|:---:|
| **1** | Modelagem em UML (diagrama de classes e de casos de uso) e implementação das classes, testando todas as funcionalidades por meio de um roteiro de testes | Terminal (`main.py`) | [Assistir](#) | `nivel 1 concluído`  | Em andamento |
| **2** | Menu funcional: o usuário navega pelas funcionalidades do sistema | Terminal (menu) | Em breve      | `nivel-2: concluído` | Pendente |
| **3** | Persistência dos dados em banco de dados | Terminal (menu) | Em breve      | `nivel-3: concluído` | Pendente |
| **4** | Interface gráfica, com o sistema funcionando em janelas | Janelas (GUI) | Em breve      | `nivel-4: concluído` | Pendente |

> **Como ler a tabela:** a coluna *Commit de entrega* mostra o nome do commit que marca o nível finalizado. Para ver o projeto naquele momento, basta procurar esse commit (ou a tag de mesmo nome) no histórico.

### Nível 1: Modelagem e testes no terminal

**Propósito:** apresentar a modelagem do sistema e provar que todas as funcionalidades funcionam.

- Diagrama de classes com herança, polimorfismo, composição, associação e dependência.
- Diagrama de casos de uso.
- Roteiro de testes (`main.py`) que percorre todas as funcionalidades e mostra também os erros que o sistema recusa.

**Vídeo de apresentação (até 3 min):** *link em breve*

### Nível 2: Menu funcional

**Propósito:** permitir que o usuário use o sistema por conta própria, escolhendo as opções em um menu no terminal.

**Vídeo de apresentação (até 6 min):** *link em breve*

### Nível 3: Banco de dados

**Propósito:** guardar clientes, funcionários, quartos e hospedagens de forma permanente, para que os dados continuem existindo depois de fechar o programa.

**Vídeo de apresentação (até 6 min):** *link em breve*

### Nível 4: Interface gráfica

**Propósito:** substituir o terminal por janelas, mantendo as mesmas funcionalidades.

**Vídeo de apresentação (até 6 min):** *link em breve*

## Funcionalidades

- **Funcionários:** cadastrar, atualizar (nome e senha), listar e remover.
- **Login:** entrar e sair do sistema, com verificação de senha.
- **Clientes:** cadastrar (com validação de CPF e bloqueio de CPF repetido), atualizar, listar e remover.
- **Quartos:** 20 quartos (10 simples e 10 duplos), com os estados livre, ocupado e em limpeza.
- **Hospedagem:** check-in com comprovante, lançamento de consumo e check-out com extrato da conta.
- **Limpeza:** enviar o quarto para limpeza ao fim da estadia e concluí-la.

## Arquitetura (ECB)

| Papel | O que faz | Onde está |
|---|---|---|
| **Entity** | Guarda os dados e as regras do próprio objeto (por exemplo, um quarto só é ocupado se estiver livre) | `Sistema/entities/` |
| **Control** | Coordena os casos de uso e as regras que envolvem vários objetos (por exemplo, CPF repetido) | `Sistema/controllers/` |
| **Boundary** | Interação com o usuário | `Sistema/main.py` |

## Diagramas UML

Os diagramas do sistema estão na pasta [`UML/`](./UML):

- Diagrama de classes
- Diagrama de casos de uso

## Estrutura

```
Sistema/
├── controllers/    Controladores (cliente, funcionário, login, quarto, hospedagem)
├── entities/       Entidades do domínio
│   ├── pessoas/    Pessoa (abstrata), Cliente e Funcionário
│   └── quarto/     Quarto (abstrata), QuartoSimples e QuartoDuplo
└── main.py         Ponto de entrada do sistema
UML/                Diagramas de classes e de casos de uso
LICENSE             Licença MIT
```

As pastas `controllers/` e `entities/` concentram as regras do sistema e são reaproveitadas em todos os níveis. O que muda de um nível para o outro é a forma de interagir com elas (`main.py`) e, a partir do Nível 3, onde os dados são guardados.

## Como executar

É necessário ter o **Python 3** instalado.

```bash
git clone https://github.com/isaacjf22/controle-hospedagem-jf.git
cd controle-hospedagem-jf/Sistema
python main.py
```

O `main.py` é o ponto de entrada e o seu comportamento depende do nível:

| Nível | O que o `main.py` faz |
|:---:|---|
| 1 | Executa um roteiro de testes que percorre todas as funcionalidades |
| 2 | Abre o menu do sistema no terminal |
| 3 | Abre o menu, com os dados guardados em banco de dados |
| 4 | Abre a interface gráfica |

Para ver o sistema exatamente como estava em um nível, use o commit de entrega indicado na [tabela de níveis](#níveis-do-projeto).

## Autor

[Isaac Ferreira](https://github.com/isaacjf22)
