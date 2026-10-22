from datetime import datetime, timedelta

from controllers.controlador_cliente import ControladorCliente
from controllers.controlador_funcionario import ControladorFuncionario
from controllers.controlador_login import ControladorLogin
from controllers.controlador_quarto import ControladorQuarto
from controllers.controlador_hospedagem import ControladorHospedagem

PAUSAR = True


def titulo(texto):
    if PAUSAR:
        input("\n[ENTER para continuar]")
    print("\n" + "=" * 50)
    print(f"  {texto}")
    print("=" * 50)


def ok(texto):
    print(f"  [OK] {texto}")


def deve_falhar(descricao, acao):
    """Executa uma ação que DEVE ser recusada e mostra a mensagem do sistema."""
    try:
        acao()
        print(f"  [FALHA] {descricao}: deveria ter sido recusado!")
    except ValueError as erro:
        print(f"  [RECUSADO] {descricao} -> {erro}")


def mostrar_clientes(ctl):
    for c in ctl.listar_clientes():
        print(f"    {c.id}) {c.nome} - CPF {c.cpf}")


def mostrar_funcionarios(ctl):
    for f in ctl.listar_funcionarios():
        print(f"    {f.id}) {f.nome} - CPF {f.cpf}")


def mostrar_quartos(ctl, numeros):
    for n in numeros:
        q = ctl.buscar_quarto(n)
        print(f"    Quarto {q.numeroQuarto} ({type(q).__name__}) - {q.statusQuarto.value}")


def mostrar_hospedagens(ctl):
    ativas = ctl.listar_hospedagens_ativas()
    if not ativas:
        print("    (nenhuma hospedagem ativa)")
    for h in ativas:
        print(f"    {h.id}) {h.cliente.nome} - quarto {h.quarto.numeroQuarto}")


# ---------- montagem do sistema ----------

ctl_cliente = ControladorCliente()
ctl_funcionario = ControladorFuncionario()
ctl_login = ControladorLogin(ctl_funcionario)
ctl_quarto = ControladorQuarto()
ctl_hospedagem = ControladorHospedagem(ctl_cliente, ctl_quarto)


# 1. FUNCIONÁRIOS
titulo("1. Funcionários")
ctl_funcionario.cadastrar_funcionario("Carlos Souza", "11122233344", "senha123")
ctl_funcionario.cadastrar_funcionario("Beatriz Lima", "55566677788", "abcd")
ok("2 funcionários cadastrados")
mostrar_funcionarios(ctl_funcionario)

ctl_funcionario.atualizar_funcionario(2, nome="Beatriz Lima Costa")
ok("nome do funcionário 2 atualizado")
deve_falhar("senha com menos de 4 caracteres",
            lambda: ctl_funcionario.atualizar_funcionario(1, senha="12"))
deve_falhar("nova senha igual à atual",
            lambda: ctl_funcionario.atualizar_funcionario(1, senha="senha123"))

ctl_funcionario.remover_funcionario(2)
ok("funcionário 2 removido")
mostrar_funcionarios(ctl_funcionario)


# 2. LOGIN
titulo("2. Login")
deve_falhar("login com senha errada", lambda: ctl_login.login("Carlos Souza", "errada"))
deve_falhar("login de funcionário inexistente", lambda: ctl_login.login("Fulano", "1234"))
ctl_login.login("Carlos Souza", "senha123")
ok(f"logado: {ctl_login.funcionarioLogado.nome}")


# 3. CLIENTES
titulo("3. Clientes")
ctl_cliente.cadastrar_cliente("Ana Pereira", "12345678901")
ctl_cliente.cadastrar_cliente("Bruno Alves", "98765432100")
ctl_cliente.cadastrar_cliente("Clara Mendes", "45678912300")
ok("3 clientes cadastrados")
mostrar_clientes(ctl_cliente)

deve_falhar("CPF já cadastrado", lambda: ctl_cliente.cadastrar_cliente("Outra Ana", "12345678901"))
deve_falhar("CPF com letras", lambda: ctl_cliente.cadastrar_cliente("Diego", "123abc78901"))
deve_falhar("nome vazio", lambda: ctl_cliente.cadastrar_cliente("   ", "11111111111"))

ctl_cliente.atualizar_cliente(3, nome="Clara Mendes Rocha")
ok("nome do cliente 3 atualizado")
ctl_cliente.remover_cliente(2)
ok("cliente 2 removido")
mostrar_clientes(ctl_cliente)


# 4. QUARTOS
titulo("4. Quartos (1-10 simples, 11-20 duplos)")
mostrar_quartos(ctl_quarto, [1, 2, 11, 12])
deve_falhar("buscar quarto inexistente", lambda: ctl_quarto.buscar_quarto(99))


# 5. CHECK-IN
titulo("5. Check-in")
amanha = datetime.now() + timedelta(days=1)

print(ctl_hospedagem.realizar_checkin(1, 1, amanha))    # Ana, quarto simples
print(ctl_hospedagem.realizar_checkin(3, 11, amanha))   # Clara, quarto duplo

deve_falhar("quarto já ocupado", lambda: ctl_hospedagem.realizar_checkin(3, 1, amanha))
deve_falhar("saída antes da entrada",
            lambda: ctl_hospedagem.realizar_checkin(1, 2, datetime.now() - timedelta(days=1)))
deve_falhar("cliente inexistente", lambda: ctl_hospedagem.realizar_checkin(50, 2, amanha))

print("  Hospedagens ativas:")
mostrar_hospedagens(ctl_hospedagem)
mostrar_quartos(ctl_quarto, [1, 11])


# 6. CONSUMO
titulo("6. Consumo durante a estadia")
ctl_hospedagem.adicionar_consumo(1, "Água", 2, 5.00)
ctl_hospedagem.adicionar_consumo(1, "Jantar", 1, 80.00)
ok("hospedagem 1: 2 águas e 1 jantar")
deve_falhar("quantidade zero", lambda: ctl_hospedagem.adicionar_consumo(1, "Suco", 0, 8.00))
deve_falhar("valor negativo", lambda: ctl_hospedagem.adicionar_consumo(1, "Suco", 1, -8.00))
deve_falhar("hospedagem inexistente", lambda: ctl_hospedagem.adicionar_consumo(99, "Suco", 1, 8.00))


# 7. CHECK-OUT polimorfismo
titulo("7. Check-out")
print(ctl_hospedagem.realizar_checkout(1))   # simples: 250 + 10 + 80
print(ctl_hospedagem.realizar_checkout(2))   # duplo: 500
deve_falhar("check-out repetido", lambda: ctl_hospedagem.realizar_checkout(1))

print("  Hospedagens ativas:")
mostrar_hospedagens(ctl_hospedagem)
mostrar_quartos(ctl_quarto, [1, 11])


# 8. LIMPEZA
titulo("8. Limpeza")
deve_falhar("concluir limpeza de quarto livre", lambda: ctl_quarto.concluir_limpeza(5))
ctl_quarto.concluir_limpeza(1)
ctl_quarto.concluir_limpeza(11)
ok("limpeza concluída nos quartos 1 e 11")
mostrar_quartos(ctl_quarto, [1, 11])


# 9. LOGOUT
titulo("9. Logout")
ctl_login.logout()
ok(f"funcionário logado: {ctl_login.funcionarioLogado}")

print("\nFim dos testes.")
