def mdc_estendido(a, b):
    a_orig, b_orig = abs(a), abs(b)
    passos = []
    
    # MDC e Quocientes
    temp_a, temp_b = a_orig, b_orig
    quocientes = []
    while temp_b != 0:
        q = temp_a // temp_b
        r = temp_a % temp_b
        passos.append(f"Resto: {temp_a} % {temp_b} = {r} | Quociente: {temp_a} // {temp_b} = {q}")
        quocientes.append(q)
        temp_a, temp_b = temp_b, r
    
    mdc = temp_a
    
    # Coeficientes s e t (Algoritmo Estendido)
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    
    passos.append("\nIniciando Combinação Linear:")
    
    # Ajuste no loop para garantir que os passos da combinação linear apareçam
    for i, q in enumerate(quocientes):
        # O último quociente na divisão de Euclides sempre leva ao resto zero, 
        # para a combinação linear de s e t, paramos uma iteração antes do fim do processo real.
        if i == len(quocientes) - 1 and len(quocientes) > 1:
            break
            
        s_next = s0 - q * s1
        t_next = t0 - q * t1
        s0, s1 = s1, s_next
        t0, t1 = t1, t_next
        passos.append(f"Passo {i+1}: s={s1}, t={t1}")
        
    # Caso base para números iguais ou onde b=0
    if not quocientes or len(quocientes) == 1:
        if a_orig >= b_orig:
            s1, t1 = 1, 0
        else:
            s1, t1 = 0, 1
        passos.append(f"Resultado Direto: s={s1}, t={t1}")
    
    return {
        "mdc": int(mdc),
        "s": int(s1),
        "t": int(t1),
        "passos": "\n".join(passos)
    }