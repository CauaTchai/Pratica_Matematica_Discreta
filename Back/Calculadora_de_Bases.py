def valor_digito(caractere):
    if '0' <= caractere <= '9':
        return int(caractere)
    else:
        return ord(caractere.upper()) - ord('A') + 10

def caractere_digito(valor):
    if 0 <= valor <= 9:
        return str(valor)
    else:
        return chr(valor - 10 + ord('A'))

def para_decimal(numero_str, base):
    numero_str = str(numero_str).upper()
    decimal = 0
    tamanho = len(numero_str)
    for i, char in enumerate(numero_str):
        valor = valor_digito(char)
        if valor >= base:
            raise ValueError(f"Dígito '{char}' inválido para a base {base}.")
        decimal += valor * (base ** (tamanho - 1 - i))
    return decimal

def de_decimal(decimal, base_destino):
    if decimal == 0: return "0"
    if decimal < 0: return "-" + de_decimal(abs(decimal), base_destino)
    res = ""
    temp_decimal = decimal
    while temp_decimal > 0:
        res = caractere_digito(temp_decimal % base_destino) + res
        temp_decimal //= base_destino
    return res

# --- NOVA FUNÇÃO PARA CONVERSÃO COM PASSO A PASSO DETALHADO ---
def converter_base(numero_str, base_origem, base_destino):
    try:
        v_decimal = para_decimal(numero_str, base_origem)
        resultado_final = de_decimal(v_decimal, base_destino)

        passos = f"Conversão de {numero_str} (Base {base_origem}) para Base {base_destino}\n\n"
        
        # Passo 1: Levar para decimal se não for decimal
        if base_origem != 10:
            passos += f"Passo 1: Converter {numero_str} da Base {base_origem} para Decimal.\n"
            tamanho = len(str(numero_str))
            soma_str = []
            for i, char in enumerate(str(numero_str).upper()):
                val = valor_digito(char)
                potencia = tamanho - 1 - i
                soma_str.append(f"({val} * {base_origem}^{potencia})")
            passos += f"Cálculo: {' + '.join(soma_str)} = {v_decimal}\n\n"
            
        # Passo 2: Levar de decimal para o destino
        if base_destino != 10:
            passo_num = 2 if base_origem != 10 else 1
            passos += f"Passo {passo_num}: Converter {v_decimal} (Decimal) para Base {base_destino} via divisões sucessivas.\n"
            temp_dec = v_decimal
            divisoes = []
            if temp_dec == 0:
                divisoes.append(f"{temp_dec} / {base_destino} = 0, Resto = 0")
            else:
                while temp_dec > 0:
                    quociente = temp_dec // base_destino
                    resto = temp_dec % base_destino
                    divisoes.append(f"{temp_dec} / {base_destino} = {quociente}, Resto = {resto} -> '{caractere_digito(resto)}'")
                    temp_dec = quociente
            passos += "\n".join(divisoes)
            passos += f"\nLendo os restos de baixo para cima: {resultado_final}\n"

        if base_origem == 10 and base_destino == 10:
            passos += f"O número já está na base 10: {resultado_final}"

        return {"resultado": resultado_final, "passos": passos}
    except Exception as e:
        return {"error": str(e)}

# --- FUNÇÃO ATUALIZADA PARA OPERAÇÕES SEM PASSO A PASSO ---
def calcular_operacao_base(n1, n2, base, operacao):
    try:
        v1 = para_decimal(n1, base)
        v2 = para_decimal(n2, base)
        
        if operacao == '+': 
            res_dec = v1 + v2
        elif operacao == '-': 
            res_dec = v1 - v2
            if res_dec < 0:
                # Retorna erro direto caso seja negativo
                return {"error": "esse tipo de operação não é suportada"}
        elif operacao == '*': 
            res_dec = v1 * v2
        else: 
            return {"error": "Operação inválida"}

        resultado_final = de_decimal(res_dec, base)
        
        # Conforme solicitado, não exibe passos extras aqui.
        return {"resultado": resultado_final}
    except Exception as e:
        return {"error": str(e)}