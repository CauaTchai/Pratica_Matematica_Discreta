async function calcularEuclides() {
    const a = document.getElementById('valorA').value;
    const b = document.getElementById('valorB').value;
    const resBox = document.getElementById('resultadoEuclides');
    const passosBox = document.getElementById('passosEuclides');

    if(!a || !b) return alert("Preencha os valores A e B");

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
    } catch (err) { alert("Erro no servidor."); }
}

async function calcularCrivo() {
    const n = document.getElementById('limiteN').value;
    const resBox = document.getElementById('resultadoCrivo');
    const passosBox = document.getElementById('passosCrivo');

    if(!n) return alert("Preencha o limite n");

    try {
        const res = await fetch('http://127.0.0.1:5000/api/crivo', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ n: parseInt(n) })
        });
        const data = await res.json();
        resBox.innerHTML = `<strong>Primos:</strong> ${data.primos.join(', ')}`;
        resBox.classList.remove('hidden');
        passosBox.innerHTML = data.passos;
        passosBox.classList.remove('hidden');
    } catch (err) { alert("Erro no Crivo."); }
}

// Controla a troca de tela entre conversão e operação
function toggleModoCB() {
    const modo = document.querySelector('input[name="modoCB"]:checked').value;
    const blocoConversao = document.getElementById('blocoConversao');
    const blocoOperacao = document.getElementById('blocoOperacao');
    const resBox = document.getElementById('resultadoBases');
    const passosBox = document.getElementById('passosBases');
    
    // Esconder resultados ao trocar de abas
    resBox.classList.add('hidden');
    passosBox.classList.add('hidden');

    if(modo === 'conversao') {
        blocoConversao.classList.remove('hidden');
        blocoOperacao.classList.add('hidden');
    } else {
        blocoConversao.classList.add('hidden');
        blocoOperacao.classList.remove('hidden');
    }
}

// Realiza o calculo da sessão bases (Conversão ou Operação)
async function calcularBases() {
    const modo = document.querySelector('input[name="modoCB"]:checked').value;
    const resBox = document.getElementById('resultadoBases');
    const passosBox = document.getElementById('passosBases');
    
    resBox.classList.add('hidden');
    passosBox.classList.add('hidden');
    
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
        
        // Verifica se houve a tratativa de erro (ex: subtração não suportada)
        if (data.error) {
            resBox.innerHTML = `<strong>Aviso:</strong> ${data.error}`;
            resBox.classList.remove('hidden');
            return;
        }

        resBox.innerHTML = `<strong>Resultado:</strong> ${data.resultado}`;
        resBox.classList.remove('hidden');
        
        // Se a resposta contiver o detalhamento dos passos (apenas na Conversão), ele renderiza
        if (data.passos) {
            passosBox.innerHTML = data.passos;
            passosBox.classList.remove('hidden');
        }
    } catch (err) { alert(err.message || "Erro de comunicação no cálculo das Bases."); }
}