import pytest
from cpf import validar_cpf, formatar_cpf

LISTA_CPFS_VALIDOS = [
    "39422781892",
    "00000000191"
]

LISTA_CPFS_INVALIDOS = [
    "12345678901",
    "111.111.111-11",
    "123",
    "1234567890123",
    "abc",
    "",
    None
]

@pytest.fixture
def cpfs_validos():
    return LISTA_CPFS_VALIDOS

@pytest.fixture
def cpfs_invalidos():
    return LISTA_CPFS_INVALIDOS

class TestCpf:

    @pytest.mark.parametrize("cpf", LISTA_CPFS_VALIDOS)
    def test_validar_cpfs_validos(self, cpf):
        assert validar_cpf(cpf) is True

    @pytest.mark.parametrize("cpf", LISTA_CPFS_INVALIDOS)
    def test_validar_cpfs_invalidos(self, cpf):
        assert validar_cpf(cpf) is False

    def test_formatar_cpf_sucesso(self):
        cpf = "39422781892"
        esperado = "394.227.818-92"
        resultado = formatar_cpf(cpf)
        assert resultado == esperado

    def test_formatar_cpf_excecao(self):
        cpf_invalido = "12345678901"
        with pytest.raises(ValueError) as excinfo:
            formatar_cpf(cpf_invalido)
        assert "CPF inválido" in str(excinfo.value)