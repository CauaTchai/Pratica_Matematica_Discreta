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
    
    # Coeficientes s e t
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    passos.append("\nIniciando Combinação Linear:")
    
    for i in range(len(quocientes) - 1):
        q = quocientes[i]
        s_next = s0 - q * s1
        t_next = t0 - q * t1
        s0, s1 = s1, s_next
        t0, t1 = t1, t_next
        passos.append(f"Passo {i+1}: s={s1}, t={t1}")
        
    if not quocientes: s1, t1 = 1, 0
    
    return {
        "mdc": int(mdc),
        "s": int(s1),
        "t": int(t1),
        "passos": "\n".join(passos)
    }