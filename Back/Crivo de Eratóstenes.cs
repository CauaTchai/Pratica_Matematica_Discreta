using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        // Define a codificação para UTF-8 explicitamente para evitar erros de acentuação no pipe do Python
        Console.OutputEncoding = Encoding.UTF8;

        int n;
        if (args.Length > 0 && int.TryParse(args[0], out n))
        {
            if (n < 2) {
                Console.WriteLine("Nao existem numeros primos no intervalo informado.");
                return;
            }

            bool[] ehPrimo = new bool[n + 1];
            for (int i = 2; i <= n; i++) ehPrimo[i] = true;

            Console.WriteLine($"--- Inicio do Crivo para n = {n} ---");
            Console.WriteLine($"Lista inicial: {string.Join(", ", Enumerable.Range(2, n - 1))}");
            Console.WriteLine("--------------------------------------");

            for (int p = 2; p * p <= n; p++)
            {
                if (ehPrimo[p])
                {
                    Console.WriteLine($"> O numero {p} e primo. Removendo seus multiplos:");
                    
                    for (int i = p * p; i <= n; i += p)
                    {
                        if (ehPrimo[i])
                        {
                            ehPrimo[i] = false;
                            Console.WriteLine($"  [X] {i} removido (multiplo de {p})");
                        }
                    }
                }
            }

            Console.WriteLine("\n--- Processo Finalizado ---");
            Console.WriteLine("---FINAL---");

            List<int> resultado = new List<int>();
            for (int i = 2; i <= n; i++)
                if (ehPrimo[i]) resultado.Add(i);

            Console.WriteLine(string.Join(", ", resultado));
        }
    }
}