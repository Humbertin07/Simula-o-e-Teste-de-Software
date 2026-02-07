def validar_nota(nota):
    """Verifica se a nota está no intervalo entre 0 e 10."""
    return 0 <= nota <= 10

def calcular_media(notas):
    """Calcula a média ignorando notas inválidas. Erro se não houver notas válidas."""
    validas = [n for n in notas if validar_nota(n)]
    if not validas:
        raise ValueError("Lista de notas válidas vazia")
    return sum(validas) / len(validas)

def obter_situacao(media):
    """Retorna Aprovado (>=7), Recuperação (>=5) ou Reprovado (<5)."""
    if not (0 <= media <= 10):
        raise ValueError("Media invalida")
    
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperação"
    else:
        return "Reprovado"

def calcular_estatisticas(notas):
    """Gera dicionário com as métricas da turma conforme slide 17."""
    validas = [n for n in notas if validar_nota(n)]
    media = calcular_media(validas)
    situacoes = [obter_situacao(n) for n in validas]
    
    return {
        "media": media,
        "maior": float(max(validas)),
        "menor": float(min(validas)),
        "aprovados": situacoes.count("Aprovado"),
        "reprovados": situacoes.count("Reprovado"),
        "recuperacao": situacoes.count("Recuperação")
    }

def normalizar_notas(notas, nota_maxima=10):
    """Converte notas de qualquer escala para a escala de 0 a 10."""
    return [(n / nota_maxima) * 10 for n in notas]