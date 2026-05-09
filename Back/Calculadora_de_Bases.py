def valor_digito(caractere):
    """Transforma uma letra (como 'A') no seu valor numérico (10)."""
    if '0' <= caractere <= '9':
        return int(caractere)
    else:
        return ord(caractere.upper()) - ord('A') + 10

def caractere_digito(valor):
    """Transforma um número (como 15) na sua letra correspondente ('F')."""
    if 0 <= valor <= 9:
        return str(valor)
    else:
        return chr(valor - 10 + ord('A'))

def para_decimal(numero_str, base):
    """Pega um número em qualquer base e descobre quanto ele vale em Decimal."""
    numero_str = str(numero_str).upper()
    decimal = 0
    tamanho = len(numero_str)
    for i, char in enumerate(numero_str):
        valor = valor_digito(char)
        if valor >= base:
            raise ValueError(f"Dígito '{char}' não existe na base {base}.")
        # Multiplica o dígito pela base elevada à sua posição
        decimal += valor * (base ** (tamanho - 1 - i))
    return decimal

def de_decimal(decimal, base_destino):
    """Pega um valor Decimal e 'desmancha' ele para outra base usando divisões."""
    if decimal == 0: return "0"
    if decimal < 0: return "-" + de_decimal(abs(decimal), base_destino)
    res = ""
    temp_decimal = decimal
    while temp_decimal > 0:
        # O resto da divisão vira o dígito da nova base
        res = caractere_digito(temp_decimal % base_destino) + res
        temp_decimal //= base_destino
    return res

def converter_base(numero_str, base_origem, base_destino):
    """Gerencia o processo de conversão e cria o texto explicativo (passo a passo)."""
    try:
        v_decimal = para_decimal(numero_str, base_origem)
        resultado_final = de_decimal(v_decimal, base_destino)

        passos = f"Convertendo {numero_str} (Base {base_origem}) -> Base {base_destino}\n\n"
        
        # Explicação de como virou decimal
        if base_origem != 10:
            passos += f"1) Convertendo para Decimal:\n"
            tamanho = len(str(numero_str))
            soma_str = []
            for i, char in enumerate(str(numero_str).upper()):
                val = valor_digito(char)
                potencia = tamanho - 1 - i
                soma_str.append(f"({val} * {base_origem}^{potencia})")
            passos += f"Conta: {' + '.join(soma_str)} = {v_decimal}\n\n"
            
        # Explicação das divisões sucessivas
        if base_destino != 10:
            p_num = 2 if base_origem != 10 else 1
            passos += f"{p_num}) Dividindo {v_decimal} pela base destino ({base_destino}):\n"
            temp_dec = v_decimal
            divisoes = []
            while temp_dec > 0:
                quociente = temp_dec // base_destino
                resto = temp_dec % base_destino
                divisoes.append(f"{temp_dec} ÷ {base_destino} = {quociente}, sobra {resto} ('{caractere_digito(resto)}')")
                temp_dec = quociente
            passos += "\n".join(divisoes)
            passos += f"\n\nResultado (restos de baixo para cima): {resultado_final}"

        return {"resultado": resultado_final, "passos": passos}
    except Exception as e:
        return {"error": str(e)}

def calcular_operacao_base(n1, n2, base, operacao):
    """Realiza contas matematicas convertendo tudo para decimal primeiro."""
    try:
        v1 = para_decimal(n1, base)
        v2 = para_decimal(n2, base)
        
        if operacao == '+': res_dec = v1 + v2
        elif operacao == '-': 
            res_dec = v1 - v2
            if res_dec < 0: return {"error": "Resultado negativo não é suportado."}
        elif operacao == '*': res_dec = v1 * v2
        else: return {"error": "Operação inválida."}

        return {"resultado": de_decimal(res_dec, base)}
    except Exception as e:
        return {"error": str(e)}