def menu():
    escolha = 0
    while escolha != 7:
        print("Conversor de Bases Numéricas\n")
        print("1. Decimal para Binário")
        print("2. Binário para Decimal")
        print("3. Decimal para Hexadecimal")
        print("4. Hexadecimal para Decimal")
        print("5. Binário para Hexadecimal")
        print("6. Hexadecimal para Binário")
        print("7. Sair")
        print("")
        escolha = int(input("Digite sua escolha: "))
        print("")
   
        match(escolha):
            case 1:
                print("Decimal para Binário")
                print("")
                decimal = int(input("Digite um número decimal: "))
                resultado = decimal_para_binario(decimal)
                print(f"\nResultado Binário: {resultado}")
            case 2:
                print("Binário para Decimal")
                print("")
                binario = input("Digite um número binário: ")
                resultado = binario_para_decimal(binario)
                print(f"\nResultado Decimal: {resultado}")
            case 3:
                print("Decimal para Hexadecimal")
                print("")
                decimal = int(input("Digite um número decimal: "))
                resultado = decimal_para_hexadecimal(decimal)
                print(f"\nResultado Hexadecimal: {resultado}")
            case 4:
                print("Hexadecimal para Decimal")
                print("")
                hexadecimal = input("Digite um número hexadecimal: ")
                resultado = hexadecimal_para_decimal(hexadecimal)
                print(f"\nResultado Decimal: {resultado}")
            case 5:
                print("Binário para Hexadecimal")
                print("")
                binario = input("Digite um número binário: ")
                resultado = binario_para_hexadecimal(binario)
                print(f"\nResultado Hexadecimal: {resultado}")
            case 6:
                print("Hexadecimal para Binário")
                print("")
                hexadecimal = input("Digite um número hexadecimal: ")
                resultado = hexadecimal_para_binario(hexadecimal)
                print(f"\nResultado Binário: {resultado}")
            case 7:
                print("Sair")

def decimal_para_binario(decimal):
    print(f"Cálculo: Dividindo {decimal} por 2 sucessivamente")
    if decimal == 0: return "0"
    binario = ""
    passos = []
    while decimal > 0:
        resto = decimal % 2
        quociente = decimal // 2
        print(f"  {decimal} / 2 = {quociente}, Resto: {resto}")
        binario = str(resto) + binario
        passos.append(resto)
        decimal = quociente
    print(f"Restos coletados: {passos}")
    return binario

def binario_para_decimal(binario):
    print(f"Cálculo: Somando potências de 2 para o binário {binario}")
    decimal = 0
    potencia = 0
    passos = []
    # Percorre a string da direita para a esquerda
    for i in range(len(binario) - 1, -1, -1):
        bit = int(binario[i])
        valor_posicao = bit * (2 ** potencia)
        decimal = decimal + valor_posicao
        print(f"  Posição {potencia}: Bit {bit} * (2^{potencia}) = {valor_posicao}. Soma parcial: {decimal}")
        passos.append(decimal)
        potencia += 1
    print(f"Somas parciais: {passos}")
    return decimal

def decimal_para_hexadecimal(decimal):
    print(f"Cálculo: Dividindo {decimal} por 16 sucessivamente")
    if decimal == 0: return "0"
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    passos = []
    while decimal > 0:
        resto = decimal % 16
        quociente = decimal // 16
        char = hex_chars[resto]
        print(f"  {decimal} / 16 = {quociente}, Resto: {resto} -> Caractere: '{char}'")
        hexadecimal = char + hexadecimal
        passos.append(char)
        decimal = quociente
    print(f"Caracteres coletados: {passos}")
    return hexadecimal

def hexadecimal_para_decimal(hexadecimal):
    hexadecimal = hexadecimal.upper()
    print(f"Cálculo: Somando potências de 16 para o hexadecimal {hexadecimal}")
    decimal = 0
    potencia = 0
    passos = []
    # Percorre a string da direita para a esquerda
    for i in range(len(hexadecimal) - 1, -1, -1):
        char = hexadecimal[i]
        if '0' <= char <= '9':
            valor = int(char)
        else:
            # A=10, B=11, ..., F=15
            valor = ord(char) - 55
            print(f"  Mapeamento: Letra '{char}' = {valor}")
        
        valor_posicao = valor * (16 ** potencia)
        decimal = decimal + valor_posicao
        print(f"  Posição {potencia}: Valor {valor} * (16^{potencia}) = {valor_posicao}. Soma parcial: {decimal}")
        passos.append(decimal)
        potencia += 1
    print(f"Somas parciais: {passos}")
    return decimal

def binario_para_hexadecimal(binario):
    decimal = binario_para_decimal(binario)
    return decimal_para_hexadecimal(decimal)

def hexadecimal_para_binario(hexadecimal):
    decimal = hexadecimal_para_decimal(hexadecimal)
    return decimal_para_binario(decimal)

def main():
    menu()

if __name__ == "__main__":
    main()