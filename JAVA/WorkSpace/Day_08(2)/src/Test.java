
public class Test 
{
	public static void main(String[] args) 
	{
		int x = 1;
		int y = 1;
		
		try 
		{
			int result = x / y;
		} 
		catch (ArithmeticException e) 
		{
			System.out.println("I can't divide by zero");
		}
		System.out.println("This phrase... will it work?");
	}
}
