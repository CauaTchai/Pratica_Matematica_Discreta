using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        // Garante que o console aceite caracteres especiais (UTF8)
        Console.OutputEncoding = Encoding.UTF8;

        int n;
        // Tenta ler o número 'n' passado pelo Python
        if (args.Length > 0 && int.TryParse(args[0], out n))
        {
            if (n < 2) {
                Console.WriteLine("Nao existem primos menores que 2.");
                return;
            }

            // Criamos uma 'lista de presença' onde todos começam como verdadeiros
            bool[] ehPrimo = new bool[n + 1];
            for (int i = 2; i <= n; i++) ehPrimo[i] = true;

            Console.WriteLine($"--- Iniciando Crivo ate {n} ---");
            
            // Lógica do Crivo: pegamos um número e riscamos todos os seus múltiplos
            for (int p = 2; p * p <= n; p++)
            {
                if (ehPrimo[p])
                {
                    Console.WriteLine($"> {p} primo. Riscando multiplos:");
                    for (int i = p * p; i <= n; i += p)
                    {
                        if (ehPrimo[i])
                        {
                            ehPrimo[i] = false;
                            Console.WriteLine($"  [X] {i} removido.");
                        }
                    }
                }
            }

            Console.WriteLine("\n--- Fim do Processo ---");
            Console.WriteLine("---FINAL---");

            List<int> resultado = new List<int>();
            for (int i = 2; i <= n; i++)
                if (ehPrimo[i]) resultado.Add(i);

            Console.WriteLine(string.Join(", ", resultado));
        }
    }
}