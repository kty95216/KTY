
public class Test2 
{	
	public static void main(String[] args) 
	{
		int[] x = new int[10];
		
		try 
		{
			x[10] = 0;
		}
		catch (ArrayIndexOutOfBoundsException e) 
		{
			System.out.println("catch문");
		}
		System.out.println("프로그램 종료");
	}
}
