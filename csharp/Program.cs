// Методы генерации массива, вывода суммы его элементов

void Main()
    {   
        int startValue = int.Parse(Console.ReadLine());
        int endValue = int.Parse(Console.ReadLine());
        PrintSum(GetCubes(startValue, endValue));   
    }

int[] GetCubes(int a, int b)
{   
    return Enumerable.Range(a, b - a + 1).Select(e => e * e * e).ToArray();
}

void PrintSum(int[] arr)
{
    Console.WriteLine(arr.Sum());
}

Main();