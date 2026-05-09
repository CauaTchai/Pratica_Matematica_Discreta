from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import os
import sys
import Euclides_Estendido
import Calculadora_de_Bases  # <-- Corrigido o nome do import (com 's' no final)

app = Flask(__name__)
CORS(app)

@app.route('/api/euclides', methods=['POST'])
def euclides():
    data = request.json
    a = data.get('a')
    b = data.get('b')
    res = Euclides_Estendido.mdc_estendido(a, b)
    res['equacao'] = f"{res['mdc']} = {a}({res['s']}) + {b}({res['t']})"
    return jsonify(res)

@app.route('/api/crivo', methods=['POST'])
def crivo():
    data = request.json
    n = data.get('n')
    try:
        process = subprocess.Popen(['dotnet', 'run', '--project', '.', str(n)], 
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        if "---FINAL---" in stdout:
            partes = stdout.split("---FINAL---")
            passos = partes[0].strip()
            primos = [int(x.strip()) for x in partes[1].strip().split(',') if x.strip()]
            return jsonify({"passos": passos, "primos": primos})
        return jsonify({"error": "Erro no processamento do C#"}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/bases', methods=['POST'])
def bases():
    data = request.json
    tipo = data.get('tipo')
    
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
        return jsonify({"error": "Tipo de ação inválida"}), 400

    if "error" in resultado:
        return jsonify(resultado), 400
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True, port=5000)