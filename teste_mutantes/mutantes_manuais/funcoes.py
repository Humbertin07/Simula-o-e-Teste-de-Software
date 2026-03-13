# MUTAÇÃO 1: >= trocado por >
def verificar_idade(idade):
    if idade > 0 and idade < 150:
        return True
    return False


# MUTAÇÃO 2: / trocado por *
def calcular_desconto(preco, percentual):
    desconto = percentual * 100
    valor_final = preco - (preco * desconto)
    return valor_final


# MUTAÇÃO 3: == trocado por !=
def eh_numero_par(numero):
    if numero % 2 != 0:
        return True
    return False


# MUTAÇÃO 4: += trocado por -=
def somar_lista(numeros):
    total = 0
    for numero in numeros:
        total -= numero
    return total


# MUTAÇÃO 5: >= trocado por >
def maximo_entre_tres(a, b, c):
    if a > b:
        if a > c:
            return a
        return c
    if b > c:
        return b
    return c


# MUTAÇÃO 6: < trocado por <=
def verificar_idade(idade):
    if idade >= 0 and idade <= 150:
        return True
    return False


# MUTAÇÃO 7: - trocado por +
def calcular_desconto(preco, percentual):
    desconto = percentual / 100
    valor_final = preco + (preco * desconto)
    return valor_final


# MUTAÇÃO 8: == trocado por >
def eh_numero_par(numero):
    if numero % 2 > 0:
        return True
    return False


# MUTAÇÃO 9: += trocado por *=
def somar_lista(numeros):
    total = 1
    for numero in numeros:
        total *= numero
    return total


# MUTAÇÃO 10: >= trocado por <=
def maximo_entre_tres(a, b, c):
    if a <= b:
        if a <= c:
            return a
        return c
    if b <= c:
        return b
    return c
