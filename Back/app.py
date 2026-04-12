from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
# CORS permite que o front-end (index.html) acesse esta API sem bloqueios de segurança
CORS(app)

# Lógica matemática do Algoritmo de Euclides Estendido
def mdc_estendido_logic(a, b):
    a_orig, b_orig = abs(a), abs(b)
    passos = []
    temp_a, temp_b = a_orig, b_orig
    quocientes = []
    
    # Etapa 1: Encontrar o MDC e armazenar quocientes para a volta
    while temp_b != 0:
        q = temp_a // temp_b
        r = temp_a % temp_b
        passos.append(f"Resto: {temp_a} % {temp_b} = {r} | Quociente: {temp_a} // {temp_b} = {q}")
        quocientes.append(q)
        temp_a, temp_b = temp_b, r
    
    mdc = temp_a
    # Etapa 2: Retrocesso para encontrar coeficientes s e t (combinação linear)
    s0, s1, t0, t1 = 1, 0, 0, 1
    for q in quocientes[:-1]:
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
    
    if b == 0: s1, t1 = 1, 0

    return {"mdc": int(mdc), "s": int(s1), "t": int(t1), "passos": "\n".join(passos)}

# Rota para o cálculo de Euclides
@app.route('/euclides', methods=['POST'])
def euclides():
    try:
        data = request.get_json()
        return jsonify(mdc_estendido_logic(int(data['a']), int(data['b'])))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Rota para o Crivo (chama o executável C#)
@app.route('/crivo', methods=['POST'])
def crivo():
    try:
        data = request.get_json()
        limite = data.get('limite')
        
        # Chama o processo 'dotnet run' enviando o limite como argumento
        processo = subprocess.run(
            ['dotnet', 'run', '--', str(limite)], 
            capture_output=True, 
            text=True, 
            shell=True,
            encoding='utf-8' # Garante que os acentos do C# cheguem corretamente
        )
        
        saida_bruta = processo.stdout.strip()
        
        # Divide a string do C# entre a explicação (passos) e a lista final (resultado)
        if "---FINAL---" in saida_bruta:
            passos, resultado = saida_bruta.split("---FINAL---")
            return jsonify({
                "resultado_bruto": resultado.strip(), 
                "passos": passos.strip()
            })
        return jsonify({"resultado_bruto": saida_bruta, "passos": ""})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Inicia o servidor na porta 5000
    app.run(port=5000, debug=True)