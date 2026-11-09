# Controle de Hospedagem Jf

Sistema de gerenciamento de hospedagem de um hotel, desenvolvido em **Python** para a disciplina **Orientação a Objetos** do **Prof. Henrique Moura** (UnB).

O projeto evolui em quatro níveis. Cada nível entregue é marcado por um commit próprio, e o histórico do repositório mostra o sistema crescendo de um nível para o outro.

## Finalidade

Simular a rotina de um hotel: cadastro de clientes e funcionários, controle de quartos, registro de hospedagens (check-in e check-out) e lançamento de gastos dos hóspedes.

O projeto aplica herança, polimorfismo, composição, associação e dependência, com modelagem em UML no padrão **ECB** (Entity, Control, Boundary). A partir do Nível 3, os dados ficam guardados em um banco **PostgreSQL**, acessado pelo padrão **DAO** (*Data Access Object*).

## Níveis do projeto

| Nível | Propósito | Interface | Vídeo         | Commit de entrega    | Status |
|:---:|---|---|---------------|----------------------|:---:|
| **1** | Modelagem em UML (diagrama de classes e de casos de uso) e implementação das classes, testando todas as funcionalidades por meio de um roteiro de testes | Terminal (`main.py`) | [Assistir](https://youtu.be/cp6dItPyFN4) | `nivel 1 concluído`  | Concluído |
| **2** | Menu funcional: o usuário navega pelas funcionalidades do sistema | Terminal (menu) | [Assistir](https://youtu.be/zp3Zvf0HFk8) | `nivel 2 concluído` | Concluído |
| **3** | Persistência dos dados em banco de dados (PostgreSQL) | Terminal (menu) | Em breve      | `nivel-3: concluído` | Em andamento |
| **4** | Interface gráfica, com o sistema funcionando em janelas | Janelas (GUI) | Em breve      | `nivel-4: concluído` | Pendente |

> **Como ler a tabela:** a coluna *Commit de entrega* mostra o nome do commit que marca o nível finalizado. Para ver o projeto naquele momento, basta procurar esse commit (ou a tag de mesmo nome) no histórico.

### Nível 1: Modelagem e testes no terminal

**Propósito:** apresentar a modelagem do sistema e provar que todas as funcionalidades funcionam.

- Diagrama de classes com herança, polimorfismo, composição, associação e dependência.
- Diagrama de casos de uso.
- Roteiro de testes (`main.py`) que percorre todas as funcionalidades e mostra também os erros que o sistema recusa.

**Vídeo de apresentação (até 3 min):** [assistir no YouTube](https://youtu.be/cp6dItPyFN4)

### Nível 2: Menu funcional

**Propósito:** permitir que o usuário use o sistema por conta própria, escolhendo as opções em um menu no terminal.

- Tela de login, que dá acesso ao sistema e ao cadastro de funcionários.
- Menu de hospedagem: check-in, consumo, check-out, conclusão de limpeza e cadastro de clientes.
- Logout, que encerra a sessão e volta à tela de login.
- `ControladorSistema`, que monta o sistema e decide qual tela abrir. O `main.py` passa a só iniciá-lo.

**Vídeo de apresentação (até 6 min):** [assistir no YouTube](https://youtu.be/zp3Zvf0HFk8)

### Nível 3: Banco de dados

**Propósito:** guardar clientes, funcionários, quartos, hospedagens e gastos de forma permanente, para que os dados continuem existindo depois de fechar o programa.

- Banco **PostgreSQL** com cinco tabelas: `clientes`, `funcionarios`, `quartos`, `hospedagens` e `gastos`.
- Um **DAO** por tabela, com o SQL escrito à mão. Os controladores deixam de usar listas em memória e passam a chamar os DAOs.
- Senhas dos funcionários guardadas com **hash bcrypt**, nunca em texto puro.
- Funcionário administrador criado automaticamente na primeira execução, com os dados lidos do arquivo `.env`.
- Os 20 quartos cadastrados no banco por um script.
- Configuração do banco (usuário, senha) fora do código, no arquivo `.env`, que não vai para o Git.
- Script para **restaurar o sistema ao estado inicial**, útil para testes e demonstrações.

**Vídeo de apresentação (até 6 min):** *link em breve*

### Nível 4: Interface gráfica

**Propósito:** substituir o terminal por janelas, mantendo as mesmas funcionalidades.

**Vídeo de apresentação (até 6 min):** *link em breve*

## Funcionalidades

- **Funcionários:** cadastrar, atualizar (nome e senha), listar e remover. O administrador não pode ser removido.
- **Login:** entrar e sair do sistema, com verificação de senha por hash.
- **Clientes:** cadastrar (com validação de CPF e bloqueio de CPF repetido), atualizar, listar e remover. Um cliente com hospedagens registradas não pode ser removido.
- **Quartos:** 20 quartos (10 simples e 10 duplos), com os estados livre, ocupado e em limpeza.
- **Hospedagem:** check-in com comprovante, lançamento de consumo e check-out com extrato da conta (diárias mais consumo).
- **Limpeza:** enviar o quarto para limpeza ao fim da estadia e concluí-la.

## Arquitetura (ECB + DAO)

| Papel | O que faz | Onde está |
|---|---|---|
| **Entity** | Guarda os dados e as regras do próprio objeto (por exemplo, o CPF precisa ter 11 dígitos) | `Sistema/entities/` |
| **Control** | Coordena os casos de uso e as regras que envolvem vários objetos (por exemplo, CPF repetido) | `Sistema/controllers/` |
| **Boundary** | Interação com o usuário: mostra as telas, lê o que é digitado e exibe os erros. Não contém regras | `Sistema/boudaries/` |
| **DAO** | Único lugar com SQL: grava e busca os objetos no banco e os converte em entidades | `Sistema/dao/` |

O fluxo de uma ação no sistema é:

```
Fronteira  →  Controlador  →  DAO  →  PostgreSQL
 (menu)       (regras)       (SQL)    (tabelas)
```

O **`ControladorSistema`** cria os DAOs, controladores e telas e entrega a mesma instância a quem precisa. Ele também controla a navegação: abre o login e, depois do login, abre o menu do sistema. Assim, o `main.py` fica sem lógica e apenas inicia o sistema.

A conexão com o banco é aberta pela função `conectar()` (em `Sistema/database/conexao.py`), que lê as credenciais do arquivo `.env`.

No Nível 1, a fronteira era o próprio `main.py`, que rodava o roteiro de testes.

## Diagramas UML

Os diagramas do sistema estão na pasta [`UML/`](./UML):

- Diagrama de classes
- Diagrama de casos de uso

## Estrutura

```
Sistema/
├── boudaries/      Fronteiras: as telas do menu no terminal (login e hospedagem)
├── controllers/    Controladores (cliente, funcionário, login, quarto, hospedagem)
│                   e o ControladorSistema, que monta o sistema e controla a navegação
├── dao/            DAOs: o acesso ao banco de cada entidade
├── database/       Conexão com o banco e scripts (popular quartos, resetar)
├── entities/       Entidades do domínio
│   ├── pessoas/    Pessoa (abstrata), Cliente e Funcionário
│   └── quarto/     Quarto (abstrata), QuartoSimples e QuartoDuplo
└── main.py         Ponto de entrada: só inicia o ControladorSistema
UML/                Diagramas de classes e de casos de uso
schema.sql          Criação das tabelas do banco
quartos.sql         Cadastro dos 20 quartos
resetar.sql         Volta o sistema ao estado inicial
requirements.txt    Bibliotecas do projeto
.env.example        Modelo do arquivo de configuração (sem senhas)
LICENSE             Licença MIT
```

As pastas `controllers/` e `entities/` concentram as regras do sistema e são reaproveitadas em todos os níveis. O que muda de um nível para o outro é a forma de interagir com elas (as fronteiras) e, a partir do Nível 3, onde os dados são guardados.

## Como executar

### Níveis 1 e 2

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

**Primeiro acesso (Nível 2):** o sistema começa sem funcionários, e os dados ficam só na memória enquanto o programa está aberto. Na tela inicial, entre em *Gerenciar funcionários* e cadastre um funcionário (CPF com 11 dígitos e senha com pelo menos 4 caracteres). Depois, use o nome e a senha dele em *Realizar login*.

### Nível 3 (com banco de dados)

**Requisitos:** Python 3.11 ou mais novo e PostgreSQL 12 ou mais novo.

**1. Baixar o projeto e preparar o ambiente**

```bash
git clone https://github.com/isaacjf22/controle-hospedagem-jf.git
cd controle-hospedagem-jf
python -m venv .venv
source .venv/bin/activate          # fish: source .venv/bin/activate.fish
                                   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

**2. Instalar o PostgreSQL**

| Sistema | Como |
|---|---|
| Arch / CachyOS | `sudo pacman -S postgresql`, depois iniciar o serviço (`sudo systemctl enable --now postgresql`) |
| Ubuntu / Debian | `sudo apt install postgresql` |
| Windows | Instalador oficial em [postgresql.org/download](https://www.postgresql.org/download/windows/) |

No Arch, antes de iniciar o serviço pela primeira vez, é preciso inicializar o banco: `sudo -iu postgres initdb --locale=C.UTF-8 --encoding=UTF8 -D /var/lib/postgres/data`.

**3. Criar o usuário e o banco**

```bash
sudo -iu postgres psql
```
```sql
CREATE USER seu_usuario WITH PASSWORD 'sua_senha';
CREATE DATABASE db_hotel OWNER seu_usuario;
\q
```
(No Windows, abra o *SQL Shell (psql)* instalado com o PostgreSQL, ou use o pgAdmin ou o DBeaver.)

**4. Configurar o `.env`**

Copie o modelo e preencha os valores:

```bash
cp .env.example .env
```

```
DB_HOST=localhost
DB_NAME=db_hotel
DB_USER=seu_usuario
DB_PASSWORD=sua_senha

ADMIN_NOME=admin
ADMIN_CPF=00000000000
ADMIN_SENHA=uma_senha_forte
```

O arquivo `.env` guarda as senhas e **não vai para o Git** (está no `.gitignore`). As variáveis `ADMIN_*` definem o administrador criado na primeira execução: o CPF precisa ter 11 dígitos, e a senha, pelo menos 4 caracteres.

**5. Criar as tabelas e os quartos**

```bash
psql -h localhost -U seu_usuario -d db_hotel -f schema.sql
cd Sistema
python -m database.popular_quartos
```

O `schema.sql` cria as cinco tabelas, e o script cadastra os 20 quartos (1 a 10 simples, 11 a 20 duplos).

**6. Executar**

```bash
python main.py
```

Na primeira execução, o administrador é criado com os dados do `.env`. Na tela inicial, escolha *Realizar login* e use o nome e a senha definidos em `ADMIN_NOME` e `ADMIN_SENHA`. A senha fica guardada como hash no banco e só pode ser trocada depois pelo menu, em *Gerenciar funcionários*.

### Restaurar o sistema ao estado inicial

Para voltar ao começo (sem clientes, hospedagens e gastos, e com todos os quartos livres), dentro da pasta `Sistema/`:

```bash
python -m database.resetar_banco
```

O script pede a confirmação digitando `RESETAR`. O administrador e os quartos são mantidos. **A operação apaga os dados e não pode ser desfeita.**

### Problemas comuns

| Mensagem ou sintoma | Causa provável | Solução |
|---|---|---|
| `Não foi possível conectar ao banco de dados` | O PostgreSQL não está rodando, ou o `.env` está errado | Iniciar o serviço (`sudo systemctl start postgresql`) e conferir o `.env` |
| `ModuleNotFoundError: No module named 'psycopg'` | O ambiente virtual não está ativo | Ativar o `.venv` e rodar `pip install -r requirements.txt` |
| `password authentication failed` | Usuário ou senha do `.env` não conferem com o banco | Corrigir o `.env` |
| `relation "clientes" does not exist` | As tabelas não foram criadas | Rodar o `schema.sql` (passo 5) |
| `Defina ADMIN_SENHA no arquivo .env.` | Faltam as variáveis do administrador | Preencher `ADMIN_*` no `.env` |
| Lista de quartos vazia | Os quartos não foram cadastrados | Rodar `python -m database.popular_quartos` |

Para ver o sistema exatamente como estava em um nível, use o commit de entrega indicado na [tabela de níveis](#níveis-do-projeto).

## Autor

[Isaac Ferreira](https://github.com/isaacjf22)