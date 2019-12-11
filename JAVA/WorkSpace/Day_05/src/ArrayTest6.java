
public class ArrayTest6 
{
	public static void main(String[] args) 
	{
		int[] lucky = new int[6];
		
		for(int i = 0; i < lucky.length; i++)
		{
			lucky[i] = (int)(Math.random() * 45 + 1);
			for(int j = 0; j < i; j++)
			{
				if(lucky[i] == lucky[j])
				{
					i--;
				}
			}
		}
		for(int result : lucky)
		{
			System.out.print(result + " ");
		}
	}
}