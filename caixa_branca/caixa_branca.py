def verificar(n):
    if n > 0:
        if n % 2 == 0:
            return "Par positivo"
        else:
            return "Impar positivo"
    elif n < 0:
        return "Negativo"
    else:
        return "Zero"

def classificar(x):
    if x > 100:
        return "Alto"
    if x > 50:
        return "Medio"
    return "Baixo"

def acesso(idade, membro):
    if idade >= 18 and membro:
        return "Permitido"
    return "Negado"

def somar_ate(n):
    soma = 0
    for i in range(n):
        soma += i
    return soma

def percorrer_matriz(m, n):
    for i in range(m):
        for j in range(n):
            print(f"Posicao ({i}, {j})")

def analisar(numeros):
    total = 0
    for n in numeros:
        if n > 0 and n % 2 == 0:
            total += n
        elif n < 0:
            total -= 1
        else:
            continue
    if total > 10:
        return "Acima"
    return "Abaixo"

def desconto(preco, cliente_vip):
    total = preco
    if cliente_vip:
        desconto = preco * 0.2
        total = preco - desconto
    if total < 50:
        total = 50
    return total