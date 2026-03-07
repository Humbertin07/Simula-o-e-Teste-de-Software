import pytest
from caixa_branca import verificar, classificar, acesso, somar_ate, percorrer_matriz, analisar, desconto

class TestExercicio1:
    @pytest.mark.parametrize("n, esperado", [
        (2, "Par positivo"),
        (3, "Impar positivo"),
        (-5, "Negativo"),
        (0, "Zero")
    ])
    def test_verificar(self, n, esperado):
        assert verificar(n) == esperado

class TestExercicio2:
    @pytest.mark.parametrize("x, esperado", [
        (150, "Alto"),
        (75, "Medio"),
        (20, "Baixo")
    ])
    def test_classificar(self, x, esperado):
        assert classificar(x) == esperado

class TestExercicio3:
    @pytest.mark.parametrize("idade, membro, esperado", [
        (20, True, "Permitido"),
        (20, False, "Negado"),
        (15, True, "Negado"),
        (15, False, "Negado")
    ])
    def test_acesso_condicoes(self, idade, membro, esperado):
        assert acesso(idade, membro) == esperado

class TestExercicio4:
    @pytest.mark.parametrize("n, esperado", [
        (0, 0),
        (1, 0),
        (4, 6)
    ])
    def test_somar_ate(self, n, esperado):
        assert somar_ate(n) == esperado

class TestExercicio5:
    @pytest.mark.parametrize("m, n, prints_esperados", [
        (0, 0, 0),
        (2, 0, 0),
        (1, 3, 3),
        (3, 3, 9)
    ])
    def test_percorrer_matriz(self, m, n, prints_esperados, capsys):
        percorrer_matriz(m, n)
        saida = capsys.readouterr().out
        linhas = [linha for linha in saida.strip().split('\n') if linha]
        assert len(linhas) == prints_esperados

class TestExercicio6:
    @pytest.mark.parametrize("numeros, esperado", [
        ([], "Abaixo"),
        ([12], "Acima"),
        ([4, 8, -5, 3], "Acima"),
        ([-5], "Abaixo"),
        ([3], "Abaixo")
    ])
    def test_analisar(self, numeros, esperado):
        assert analisar(numeros) == esperado

class TestExercicio7:
    @pytest.mark.parametrize("preco, cliente_vip, esperado", [
        (100, True, 80),
        (40, False, 50),
        (40, True, 50),
        (100, False, 100)
    ])
    def test_desconto(self, preco, cliente_vip, esperado):
        assert desconto(preco, cliente_vip) == esperado