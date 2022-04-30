// Сортировка пузырьком

int[] num = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
// int[] num = new int [line.Length];
// for (int i = 0; i < line.Length; i++)
// {
//     num[i] = Convert.ToInt32(line[i]);
// }
for (int i = 0; i < num.Length - 1; i++)
{
    for (int j = 0; j < num.Length - 1; j++)
    {
        if (num[j] > num[j + 1])
        {
            int temp = num[j];
            num[j] = num[j + 1];
            num[j + 1] = temp;
        }
    }
}
Console.WriteLine(String.Join(' ', num));