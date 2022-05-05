// Возможные варианты решения уравнения а*b+c

int[] GetValueNum(int number)
{
    List<int> validNum = new List<int>();
    int[] valid = {2, 3, 7};
    for(int i = 2; i <= number; i++)
    {
        bool flag = true;
        int data = i;
        while (data > 0)
        {
            if (valid.Contains(data % 10) != true) 
            {
                flag = false;
                break;
            }
            data /= 10;
        }
        if(flag) validNum.Add(i);
    }
    return validNum.ToArray();
}

void VasyaStyle(int number)
{
    int[] num = GetValueNum(number);
    for (int i = 0; i < num.Length; i++)
    {
        for (int j = i; j < num.Length; j++)
        {
            for (int k = 0; k < num.Length; k++)
            {
                if (number == num[i] * num[j] + num[k]) System.Console.WriteLine($"{number} = {num[i]} * {num[j]} + {num[k]}");
            }
        }
    }
}