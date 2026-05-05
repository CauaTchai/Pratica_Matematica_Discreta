def valor_digito(caractere):
    """Converte um caractere para seu valor numérico correspondente."""
    if '0' <= caractere <= '9':
        return int(caractere)
    else:
        return ord(caractere.upper()) - ord('A') + 10

def caractere_digito(valor):
    """Converte um valor numérico para seu caractere correspondente na base."""
    if 0 <= valor <= 9:
        return str(valor)
    else:
        return chr(valor - 10 + ord('A'))

def converter_base(numero_str, base_origem, base_destino):
    """
    Converte um número de uma base de origem para uma base de destino.
    Retorna um dicionário com o resultado final e o passo a passo.
    """
    numero_str = str(numero_str).upper()
    passos = f"--- Iniciando conversão de {numero_str} (Base {base_origem}) para Base {base_destino} ---\n\n"

    # Passo 1: Converter da Base Origem para Decimal (Base 10)
    decimal = 0
    if base_origem != 10:
        passos += f"1) Convertendo {numero_str} da base {base_origem} para decimal (base 10):\n"
        tamanho = len(numero_str)
        
        for i, char in enumerate(numero_str):
            potencia = tamanho - 1 - i
            valor = valor_digito(char)
            
            # Validação se o dígito pertence à base informada
            if valor >= base_origem:
                return {"error": f"Dígito '{char}' inválido para a base {base_origem}."}
            
            termo = valor * (base_origem ** potencia)
            decimal += termo
            passos += f"   - Dígito '{char}' ({valor}) * {base_origem}^{potencia} = {termo}\n"
            
        passos += f"   > Total em decimal: {decimal}\n\n"
    else:
        try:
            decimal = int(numero_str)
            passos += f"1) O número já está em decimal: {decimal}\n\n"
        except ValueError:
            return {"error": "Número inválido para a base 10."}

    # Passo 2: Converter do Decimal para a Base Destino
    if base_destino == 10:
        resultado_final = str(decimal)
        passos += f"2) A base de destino já é 10. O resultado final é: {resultado_final}\n"
        return {"resultado": resultado_final, "passos": passos}

    passos += f"2) Convertendo o decimal {decimal} para a base {base_destino} (divisões sucessivas):\n"
    
    if decimal == 0:
        resultado_final = "0"
        passos += "   > O número é 0, o resultado é 0.\n"
    else:
        num_atual = decimal
        digitos_resultado = []
        
        while num_atual > 0:
            resto = num_atual % base_destino
            quociente = num_atual // base_destino
            char_resto = caractere_digito(resto)
            
            passos += f"   - {num_atual} ÷ {base_destino} = {quociente} (Resto: {resto} -> '{char_resto}')\n"
            
            digitos_resultado.append(char_resto)
            num_atual = quociente
        
        # Inverte a lista de restos para formar o número final
        resultado_final = "".join(reversed(digitos_resultado))
        passos += f"\n   > Lendo os restos de baixo para cima, obtemos: {resultado_final}\n"

    return {
        "resultado": resultado_final,
        "passos": passos
    }