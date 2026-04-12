using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        // Garante que a saída do terminal use acentuação correta (UTF-8)
        Console.OutputEncoding = Encoding.UTF8;

        int n;
        // Tenta ler o limite 'n' enviado como argumento pelo Python (app.py)
        if (args.Length > 0 && int.TryParse(args[0], out n))
        {
            // O crivo começa a partir do número 2
            if (n < 2) {
                Console.WriteLine("Não existem números primos no intervalo informado.");
                return;
            }

            // Cria um array de booleanos onde 'true' significa que o índice é primo
            bool[] ehPrimo = new bool[n + 1];
            for (int i = 2; i <= n; i++) ehPrimo[i] = true;

            // Início da explicação visual do processo
            Console.WriteLine($"--- Início do Crivo para n = {n} ---");
            Console.WriteLine($"Lista inicial: {string.Join(", ", Enumerable.Range(2, n - 1))}");
            Console.WriteLine("--------------------------------------");

            // Algoritmo do Crivo: itera de 2 até a raiz quadrada de n
            for (int p = 2; p * p <= n; p++)
            {
                // Se o número atual ainda está marcado como primo
                if (ehPrimo[p])
                {
                    Console.WriteLine($"\n> O número {p} é primo. Removendo seus múltiplos:");
                    
                    // Marca todos os múltiplos de p como 'false' (não primos)
                    for (int i = p * p; i <= n; i += p)
                    {
                        if (ehPrimo[i])
                        {
                            ehPrimo[i] = false;
                            Console.WriteLine($"  [X] {i} removido (múltiplo de {p})");
                        }
                    }
                }
            }

            Console.WriteLine("\n--- Processo Finalizado ---");
            
            // Marcador especial que o Python usa para separar logs de resultados
            Console.WriteLine("---FINAL---");

            // Filtra e armazena apenas os números que sobraram como 'true'
            List<int> resultado = new List<int>();
            for (int i = 2; i <= n; i++)
                if (ehPrimo[i]) resultado.Add(i);

            // Exibe o resultado final separado por vírgulas
            Console.WriteLine(string.Join(", ", resultado));
        }
    }
}