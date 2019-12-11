
public class nestedlooptest3 
{
	public static void main(String[] args) 
	{
		for(int i = 1 ; i<=5 ; i++)
		{
			for(int x = i; x < 5 ; x++)
			{
				System.out.print(" ");
			}
			for(int j = 0; j < i ; j++)
			{
				System.out.print("*");
			}
			System.out.println();
		}
	}
}
