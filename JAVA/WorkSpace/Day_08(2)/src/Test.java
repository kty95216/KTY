
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
			System.out.println("0으로 못나누나보네ㅜㅜ");
		}
		System.out.println("이 구문... 실행 될까요?");
	}
}
