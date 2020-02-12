import java.util.Scanner;

public class SwitchTest 
{
	public static void main(String[] args) 
	{
		int number;
		
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter number: ");
		number = scan.nextInt();
		
		switch(number)
		{
		case 0:
			System.out.println("None");
			break;
		case 1:
			System.out.println("One");
			break;
		case 2:
			System.out.println("Two");
			break;
		default:
			System.out.println("Many");
			break;
		}
	}
}
