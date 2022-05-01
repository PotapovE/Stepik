// Елочка

int height = int.Parse(Console.ReadLine());
for (int i = 1; i <= height; ++i)
{
    string spaces = new string(' ', height - i);
    string mirrorPart = new string ('*', i - 1);
    Console.WriteLine($"{spaces}{mirrorPart}*{mirrorPart}");
}