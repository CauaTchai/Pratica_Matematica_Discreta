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
    } catch (err) {
        alert("Erro ao conectar com o servidor. Verifique se o Back-end está rodando.");
    }
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
        
        if(data.error) throw new Error(data.error);

        resBox.innerHTML = `<strong>Primos encontrados:</strong> ${data.primos.join(', ')}`;
        resBox.classList.remove('hidden');

        passosBox.innerHTML = data.passos;
        passosBox.classList.remove('hidden');
    } catch (err) {
        alert("Erro no Crivo: " + err.message);
    }
}

async function calcularBases() {
    const numero = document.getElementById('numeroBase').value;
    const baseOrigem = document.getElementById('baseOrigem').value;
    const baseDestino = document.getElementById('baseDestino').value;
    
    const resBox = document.getElementById('resultadoBases');
    const passosBox = document.getElementById('passosBases');

    if(!numero || !baseOrigem || !baseDestino) return alert("Preencha todos os campos");

    try {
        const res = await fetch('http://127.0.0.1:5000/api/bases', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 
                numero: numero, 
                base_origem: parseInt(baseOrigem), 
                base_destino: parseInt(baseDestino) 
            })
        });
        
        const data = await res.json();
        
        if(data.error) {
            alert(data.error);
            return;
        }

        resBox.innerHTML = `<strong>Resultado:</strong> ${data.resultado}`;
        resBox.classList.remove('hidden');

        if (data.passos) {
            passosBox.innerHTML = data.passos;
            passosBox.classList.remove('hidden');
        }
    } catch (err) {
        alert("Erro na conversão de bases.");
    }
}