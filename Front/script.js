// URL onde o servidor Flask está rodando
const API_URL = "http://127.0.0.1:5000";

// Função para processar o MDC Estendido
async function executarEuclides() {
    const a = document.getElementById('numA').value;
    const b = document.getElementById('numB').value;
    const resBox = document.getElementById('resEuclides');
    const stepBox = document.getElementById('stepEuclides');

    // Envia os números para a rota /euclides do Python
    const response = await fetch(`${API_URL}/euclides`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ a, b })
    });

    const result = await response.json();
    
    // Torna visíveis as caixas de resultado e passos
    resBox.classList.remove('hidden');
    stepBox.classList.remove('hidden');
    
    // Exibe o MDC e a fórmula da combinação linear
    resBox.innerHTML = `<strong>MDC:</strong> ${result.mdc}<br><small>${result.mdc} = (${result.s})*(${a}) + (${result.t})*(${b})</small>`;
    // Exibe o passo a passo textual
    stepBox.innerText = result.passos;
}

// Função para processar o Crivo de Eratóstenes
async function executarCrivo() {
    const limite = document.getElementById('limiteCrivo').value;
    const resBox = document.getElementById('resCrivo');
    const stepBox = document.getElementById('stepCrivo');

    // Reseta a visibilidade antes de uma nova consulta
    resBox.classList.add('hidden');
    stepBox.classList.add('hidden');

    try {
        const response = await fetch(`${API_URL}/crivo`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ limite: parseInt(limite) })
        });

        const data = await response.json();
        resBox.classList.remove('hidden');
        stepBox.classList.remove('hidden');

        if (response.ok) {
            // Exibe a lista final de primos
            resBox.innerHTML = `<strong>Primos encontrados:</strong> ${data.resultado_bruto}`;
            // Exibe a narração de remoção vinda do C#
            stepBox.innerText = data.passos;
        } else {
            resBox.innerHTML = `<strong>Erro:</strong> ${data.error}`;
        }
    } catch (err) {
        alert("Erro ao conectar ao servidor Flask. Verifique se o app.py está rodando.");
    }
}