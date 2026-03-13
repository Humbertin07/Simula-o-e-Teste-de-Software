"""
Testes pytest para validar as 5 funções do programa.
Contém 10 casos de teste.
"""

import pytest
from funcoes import (
    verificar_idade,
    calcular_desconto,
    eh_numero_par,
    somar_lista,
    maximo_entre_tres
)


# Testes para verificar_idade
def test_verificar_idade_valida():
    """Teste 1: Idade válida (25 anos)"""
    assert verificar_idade(25) == True


def test_verificar_idade_invalida_negativa():
    """Teste 2: Idade inválida (negativa)"""
    assert verificar_idade(-5) == False


def test_verificar_idade_invalida_maior_150():
    """Teste 3: Idade inválida (> 150)"""
    assert verificar_idade(150) == False


# Testes para calcular_desconto
def test_calcular_desconto_10_percent():
    """Teste 4: Desconto de 10% em R$100"""
    resultado = calcular_desconto(100, 10)
    assert resultado == 90.0


def test_calcular_desconto_25_percent():
    """Teste 5: Desconto de 25% em R$80"""
    resultado = calcular_desconto(80, 25)
    assert resultado == 60.0


# Testes para eh_numero_par
def test_eh_numero_par_par():
    """Teste 6: Número par (4)"""
    assert eh_numero_par(4) == True


def test_eh_numero_par_impar():
    """Teste 7: Número ímpar (7)"""
    assert eh_numero_par(7) == False


# Testes para somar_lista
def test_somar_lista_positivos():
    """Teste 8: Soma de números positivos [1, 2, 3]"""
    assert somar_lista([1, 2, 3]) == 6


def test_somar_lista_vazia():
    """Teste 9: Soma de lista vazia"""
    assert somar_lista([]) == 0


# Testes para maximo_entre_tres
def test_maximo_entre_tres():
    """Teste 10: Máximo entre 3, 7, 5"""
    assert maximo_entre_tres(3, 7, 5) == 7
