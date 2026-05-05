from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import os
import sys

# Garante que o Python encontre os módulos locais
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    import Euclides_Estendido
    import Calculadora_de_Bases
except ImportError as e:
    print(f"Erro ao importar módulos: {e}")

app = Flask(__name__)
# Configuração vital para o Front-end conseguir acessar o Back-end
CORS(app)

@app.route('/api/euclides', methods=['POST'])
def euclides():
    data = request.json
    a = data.get('a')
    b = data.get('b')
    res = Euclides_Estendido.mdc_estendido(a, b)
    # Formata a equação final: MDC = a(s) + b(t)
    res['equacao'] = f"{res['mdc']} = {a}({res['s']}) + {b}({res['t']})"
    return jsonify(res)

@app.route('/api/crivo', methods=['POST'])
def crivo():
    data = request.json
    n = data.get('n')
    
    try:
        # Executa o arquivo C# (Necessário ter o .NET SDK instalado e o arquivo compilado ou rodar via 'dotnet run')
        # Se você compilou para .exe, mude para ["./Crivo.exe", str(n)]
        process = subprocess.Popen(['dotnet', 'run', '--project', '.', str(n)], 
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        if "---FINAL---" in stdout:
            partes = stdout.split("---FINAL---")
            passos = partes[0].strip()
            primos = [int(x.strip()) for x in partes[1].strip().split(',') if x.strip()]
            return jsonify({"passos": passos, "primos": primos})
        
        return jsonify({"error": "Erro no processamento do C#", "details": stdout}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/bases', methods=['POST'])
def bases():
    data = request.json
    numero = data.get('numero')
    base_origem = data.get('base_origem')
    base_destino = data.get('base_destino')
    
    try:
        resultado_conversao = Calculadora_de_Bases.converter_base(numero, base_origem, base_destino)
        return jsonify(resultado_conversao)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)