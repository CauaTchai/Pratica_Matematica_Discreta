# 🧮 Laboratório de Matemática Discreta

Este projeto é uma aplicação Full-Stack que visualiza algoritmos fundamentais da matemática discreta. Desenvolvido para facilitar o entendimento de processos como o MDC Estendido, Números Primos e Conversão de Bases.

## 👥 Autores
* **Arthur Candido**
* **Caua de Moraes**
* **Mateus Soier**

## 🛠️ Tecnologias Utilizadas
* **Frontend:** HTML5, CSS3 (Grid/Flexbox), JavaScript (Fetch API)
* **Backend:** Python (Flask)
* **Algoritmos:** Python e C# (.NET)


## 🚀 Como Executar o Projeto

### 1. Configurar o Backend (Python)
Certifique-se de ter o Python instalado. No terminal, dentro da pasta `Back`:
pip install flask flask-cors
python app.py

O servidor iniciará em: http://127.0.0.1:5000

2. Configurar o C# (Crivo)
Dentro da pasta Back, prepare o ambiente para o algoritmo de Eratóstenes:
dotnet new console --force

# Você pode apagar o arquivo Program.cs criado automaticamente pelo comando acima.

3. Abrir o Site
Basta abrir o arquivo index.html usando a extensão Live Server do VS Code.

📖 Funcionalidades
1. Euclides EstendidoCalcula o MDC de dois números.Mostra a combinação linear (coeficientes $s$ e $t$).Exibe o passo a passo das divisões.

2. Crivo de EratóstenesEncontra todos os primos até um limite $n$.Executado via C# para alta performance.Mostra o processo de "riscar" os múltiplos em tempo real.

3. Calculadora de BasesConversão: Entre Decimal, Binário e Hexadecimal com detalhamento matemático.Operações: Soma, Subtração e Multiplicação diretamente na base escolhida.