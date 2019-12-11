
public class nestedlooptest2 
{
	public static void main(String[] args) 
	{
		for(int i = 1 ; i<=5 ; i++)
		{
			for(int x = 0 ; x<i ; x++)
			{
				System.out.print("*");
			}
			System.out.println();
		}
	}
}
