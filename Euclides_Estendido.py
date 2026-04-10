def mdc(a,b):
    a, b = abs(a), abs(b) # transforma os números inteiros - para +
    lista_quociente = []
    

    if b == 0:
        return a,  lista_quociente # evitar o erro de divisao por zero
    
    while b != 0:

        quociente = a // b
        resto = a % b
        lista_quociente.append(quociente) # guardar o quociente
        
        print(f"R: ({a}) % ({b}) = {resto}")
        print(f"Q: ({a}) // ({b}) = {quociente}")

        a, b = b, resto # atualiza a e b
    
    return a, lista_quociente # retorna mdc, lista de quocientes

def euclides_estendido(a,b):
    

    mdc_resultado, quocientes = (mdc(a,b))

    """
    Mj+1 = Mj-1 + Qj+1 * Mj
    Nj+1 = Nj-1 + Qj+1 * Nj
    """

    if len(quocientes) == 0:

        m_final = 1 if a >= 0 else -1 # Se a equação é a*m + 0*n = a, então m = 1 (ou -1 se 'a' for negativo) e n = 0.

        return mdc_resultado, m_final, 0
    
    m = [1,0]
    n = [0,1]

    for x in range(len(quocientes) - 1): # não iterar sobre o último quociente
        
        m.append(m[x] - (quocientes[x] * m[x+1]))
        n.append(n[x] - (quocientes[x] * n[x+1]))

    # pegar os ultimos elemntos da lista
    m_final = m[-1] 
    n_final = n[-1]

    # inverte os sinais se as entradas originais eram negativas
    if a < 0:
        m_final = -m_final
    if b < 0:
        n_final = -n_final
    
    return mdc_resultado, m_final, n_final