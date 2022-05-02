// Часы

int n = int.Parse(Console.ReadLine());
int hour = n % 12;
int min = hour * 5 + 5;
int dop = min / 12;
int find = min + dop;
if (find != dop) find += 1;
if (find >= 60) 
{
   find -= 60; 
   hour = (hour + 1) % 12;
}
Console.WriteLine(find < 10 ? $"{hour}:0{find}": $"{hour}:{find}");