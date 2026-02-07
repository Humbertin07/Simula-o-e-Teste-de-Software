import pytest
from notas import *

class TestSistemaNotas:
    
    # 10 TESTES: Valida notas no limite, no meio e fora do range (Slide 19)
    @pytest.mark.parametrize("nota, esperado", [
        (0, True), (5, True), (10, True), (7.5, True), (2.5, True),
        (-1, False), (11, False), (15, False), (-0.5, False), (10.1, False)
    ])
    def test_validar_nota_variadas(self, nota, esperado):
        assert validar_nota(nota) == esperado

    # 9 TESTES: Cobre as 3 situações de aprovação com valores limite (Slide 16)
    @pytest.mark.parametrize("media, situacao", [
        (7.0, "Aprovado"), (8.5, "Aprovado"), (10.0, "Aprovado"),
        (5.0, "Recuperação"), (6.0, "Recuperação"), (6.9, "Recuperação"),
        (0.0, "Reprovado"), (3.0, "Reprovado"), (4.9, "Reprovado")
    ])
    def test_situacoes_limite(self, media, situacao):
        assert obter_situacao(media) == situacao

    # 1 TESTE: Média com valores simples
    def test_media_comum(self):
        assert calcular_media([6, 8, 10]) == 8.0

    # 1 TESTE: Média filtrando as notas que não prestam (Slide 15)
    def test_media_com_filtro(self):
        assert calcular_media([5, 15, -2]) == 5.0

    # 1 TESTE: Exceção para lista vazia (Slide 7)
    def test_erro_media_vazia(self):
        with pytest.raises(ValueError):
            calcular_media([])

    # 1 TESTE: Exceção para média impossível (Slide 7)
    def test_erro_situacao_invalida(self):
        with pytest.raises(ValueError):
            obter_situacao(-5)

    # 1 TESTE: Normalização com approx para não dar erro de float (Slide 12)
    def test_normalizacao_escala(self):
        resultado = normalizar_notas([10, 20], 20)
        assert resultado == [pytest.approx(5.0), 10.0]

    # 1 TESTE: Estatísticas completas usando o padrão AAA (Slide 21)
    def test_estatisticas_turma(self):
        # Arrange
        notas = [2, 5, 8]
        # Act
        res = calcular_estatisticas(notas)
        # Assert
        assert res["media"] == 5.0
        assert res["maior"] == 8.0
        assert res["aprovados"] == 1