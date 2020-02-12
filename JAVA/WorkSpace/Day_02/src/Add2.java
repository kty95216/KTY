import java.util.Scanner;

public class Add2
{
	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);
		
		int x;
		int y;
		int sum;
		
		System.out.println("Enter the x value: ");
		x = input.nextInt();
		System.out.println("Enter the y value: ");
		y = input.nextInt();
		
		sum = x + y;
		
		System.out.println("x + y = " + sum);
	}
}
