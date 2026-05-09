from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import os
import sys
import Euclides_Estendido
import Calculadora_de_Bases

app = Flask(__name__)
# O CORS permite que o seu site (Frontend) converse com este servidor (Backend)
CORS(app)

@app.route('/api/euclides', methods=['POST'])
def euclides():
    """Rota para calcular o MDC Estendido usando lógica em Python."""
    data = request.json
    a = data.get('a')
    b = data.get('b')
    
    # Chama a função que faz o cálculo do MDC e retorna os coeficientes s e t
    res = Euclides_Estendido.mdc_estendido(a, b)
    
    # Monta a frase da combinação linear para exibir no site
    res['equacao'] = f"{res['mdc']} = {a}({res['s']}) + {b}({res['t']})"
    return jsonify(res)

@app.route('/api/crivo', methods=['POST'])
def crivo():
    """Rota que chama o programa em C# para calcular números primos."""
    data = request.json
    n = data.get('n')
    try:
        # Executa o comando 'dotnet run' passando o número limite como argumento
        process = subprocess.Popen(['dotnet', 'run', '--project', '.', str(n)], 
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        
        # O C# imprime "---FINAL---" para separar a explicação dos números primos reais
        if "---FINAL---" in stdout:
            partes = stdout.split("---FINAL---")
            passos = partes[0].strip()
            primos = [int(x.strip()) for x in partes[1].strip().split(',') if x.strip()]
            return jsonify({"passos": passos, "primos": primos})
        
        return jsonify({"error": "Ocorreu um erro dentro do processamento em C#"}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/bases', methods=['POST'])
def bases():
    """Rota para conversão de bases ou operações (soma, sub, mult)."""
    data = request.json
    tipo = data.get('tipo')
    
    # Verifica se o usuário quer converter um número ou fazer uma conta
    if tipo == 'conversao':
        resultado = Calculadora_de_Bases.converter_base(
            data.get('numero'), 
            int(data.get('base_origem')), 
            int(data.get('base_destino'))
        )
    elif tipo == 'operacao':
        resultado = Calculadora_de_Bases.calcular_operacao_base(
            data.get('n1'), 
            data.get('n2'), 
            int(data.get('base')), 
            data.get('operacao')
        )
    else:
        return jsonify({"error": "Ação inválida"}), 400

    if "error" in resultado:
        return jsonify(resultado), 400
    return jsonify(resultado)

if __name__ == '__main__':
    # Inicia o servidor na porta 5000
    app.run(debug=True, port=5000)