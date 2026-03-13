def verificar_idade(idade):
    """
    Verifica se a idade é válida (maior ou igual a 0 e menor que 150).
    """
    if idade >= 0 and idade < 150:
        return True
    return False


def calcular_desconto(preco, percentual):
    """
    Calcula o valor final após aplicar desconto.
    Exemplo: preco=100, percentual=10 retorna 90.0
    """
    desconto = percentual / 100
    valor_final = preco - (preco * desconto)
    return valor_final


def eh_numero_par(numero):
    """
    Verifica se um número é par.
    """
    if numero % 2 == 0:
        return True
    return False


def somar_lista(numeros):
    """
    Soma todos os números de uma lista.
    Exemplo: [1, 2, 3] retorna 6
    """
    total = 0
    for numero in numeros:
        total += numero
    return total


def maximo_entre_tres(a, b, c):
    """
    Retorna o maior valor entre três números.
    """
    if a >= b:
        if a >= c:
            return a
        return c
    if b >= c:
        return b
    return c
