import re

def validar_cpf(cpf: str) -> bool:
    if not isinstance(cpf, str):
        return False
    
    cpf_limpo = re.sub(r'\D', '', cpf)
    
    if len(cpf_limpo) != 11 or cpf_limpo == cpf_limpo[0] * 11:
        return False
    
    for i in range(9, 11):
        soma = sum(int(cpf_limpo[j]) * ((i + 1) - j) for j in range(i))
        digito = (soma * 10) % 11
        if (0 if digito == 10 else digito) != int(cpf_limpo[i]):
            return False
            
    return True

def formatar_cpf(cpf: str) -> str:
    if not validar_cpf(cpf):
        raise ValueError("CPF inválido")
    
    cpf_limpo = re.sub(r'\D', '', cpf)
    return f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:]}"