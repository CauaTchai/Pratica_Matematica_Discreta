// Função auxiliar para garantir que o número é inteiro e positivo
function validarPositivo(valor) {
    const n = parseInt(valor);
    return !isNaN(n) && n >= 0;
}

async function calcularEuclides() {
    const a = document.getElementById('valorA').value;
    const b = document.getElementById('valorB').value;
    const resBox = document.getElementById('resultadoEuclides');
    const passosBox = document.getElementById('passosEuclides');

    if(!validarPositivo(a) || !validarPositivo(b)) return alert("Por favor, insira números inteiros positivos.");

    try {
        const res = await fetch('http://127.0.0.1:5000/api/euclides', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ a: parseInt(a), b: parseInt(b) })
        });
        const data = await res.json();
        resBox.innerHTML = `<strong>MDC: ${data.mdc}</strong><br>${data.equacao}`;
        resBox.classList.remove('hidden');
        passosBox.innerHTML = data.passos;
        passosBox.classList.remove('hidden');
    } catch (err) { alert("Erro ao conectar com o servidor."); }
}

async function calcularCrivo() {
    const n = document.getElementById('limiteN').value;
    const resBox = document.getElementById('resultadoCrivo');
    const passosBox = document.getElementById('passosCrivo');

    if(!validarPositivo(n) || n < 2) return alert("Insira um limite maior ou igual a 2.");

    try {
        const res = await fetch('http://127.0.0.1:5000/api/crivo', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ n: parseInt(n) })
        });
        const data = await res.json();
        resBox.innerHTML = `<strong>Primos encontrados:</strong><br>${data.primos.join(', ')}`;
        resBox.classList.remove('hidden');
        passosBox.innerHTML = data.passos;
        passosBox.classList.remove('hidden');
    } catch (err) { alert("Erro ao calcular o Crivo."); }
}

function toggleModoCB() {
    const modo = document.querySelector('input[name="modoCB"]:checked').value;
    document.getElementById('blocoConversao').classList.toggle('hidden', modo !== 'conversao');
    document.getElementById('blocoOperacao').classList.toggle('hidden', modo !== 'operacao');
    document.getElementById('resultadoBases').classList.add('hidden');
    document.getElementById('passosBases').classList.add('hidden');
}

async function calcularBases() {
    const modo = document.querySelector('input[name="modoCB"]:checked').value;
    const resBox = document.getElementById('resultadoBases');
    const passosBox = document.getElementById('passosBases');
    
    let payload = {};
    if (modo === 'conversao') {
        payload = {
            tipo: 'conversao',
            numero: document.getElementById('numConv').value,
            base_origem: document.getElementById('baseOrigem').value,
            base_destino: document.getElementById('baseDestino').value
        };
    } else {
        payload = {
            tipo: 'operacao',
            base: document.getElementById('baseOpSel').value,
            n1: document.getElementById('val1').value,
            n2: document.getElementById('val2').value,
            operacao: document.getElementById('opSel').value
        };
    }

    try {
        const res = await fetch('http://127.0.0.1:5000/api/bases', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        const data = await res.json();
        
        if (data.error) {
            resBox.innerHTML = `<strong>Erro:</strong> ${data.error}`;
        } else {
            resBox.innerHTML = `<strong>Resultado:</strong> ${data.resultado}`;
            if (data.passos) {
                passosBox.innerHTML = data.passos;
                passosBox.classList.remove('hidden');
            }
        }
        resBox.classList.remove('hidden');
    } catch (err) { alert("Erro na Calculadora de Bases."); }
}