
public class ifExample3 
{
	public static void main(String[] args) 
	{
		//Math라는 꾸러미는 수학적인 기능들을 담고있어요...
		//Math.random(); <- 0.00000000~0.99999999 까지의 임의의 숫자를 생성해줌
		int num1;
		
		num1 = (int)(Math.random() * 6 + 1);
		System.out.println(num1);
		
		if(num1 == 1)
			System.out.println("1나옴");
		else if(num1 == 2)
			System.out.println("2나옴");
		else if(num1 == 3)
			System.out.println("3나옴");
		else if(num1 == 4)
			System.out.println("4나옴");
		else if(num1 == 5)
			System.out.println("5나옴");
		else
			System.out.println("6나옴");
				
	}
}