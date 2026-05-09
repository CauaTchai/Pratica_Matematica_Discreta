def mdc_estendido(a, b):
    """Calcula o MDC e os coeficientes s e t (combinação linear)."""
    a_orig, b_orig = abs(a), abs(b)
    passos = []
    
    # Primeira fase: Divisões sucessivas (Euclides clássico)
    temp_a, temp_b = a_orig, b_orig
    quocientes = []
    while temp_b != 0:
        q = temp_a // temp_b
        r = temp_a % temp_b
        passos.append(f"Divisão: {temp_a} = {temp_b} * ({q}) + {r}")
        quocientes.append(q)
        temp_a, temp_b = temp_b, r
    
    mdc = temp_a
    
    # Segunda fase: Voltando para achar s e t
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    
    passos.append("\nCalculando coeficientes (s, t):")
    
    for i, q in enumerate(quocientes):
        if i == len(quocientes) - 1 and len(quocientes) > 1:
            break
            
        s_next = s0 - q * s1
        t_next = t0 - q * t1
        s0, s1 = s1, s_next
        t0, t1 = t1, t_next
        passos.append(f"Passo {i+1}: s = {s1}, t = {t1}")
        
    # Ajuste para casos simples (ex: b=0)
    if not quocientes or len(quocientes) == 1:
        if a_orig >= b_orig: s1, t1 = 1, 0
        else: s1, t1 = 0, 1
    
    return {
        "mdc": int(mdc),
        "s": int(s1),
        "t": int(t1),
        "passos": "\n".join(passos)
    }