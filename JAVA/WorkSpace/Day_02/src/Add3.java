import java.util.Scanner;

public class Add3
{
	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);
		
		double korean = 0;
		double english = 0;
		double math = 0;
		double computer = 0;
		double sum = 0;
		double average = 0;
		
		System.out.println("Korean Score: ");
		korean = input.nextInt();
		System.out.println("English Score: ");
		english = input.nextInt();
		System.out.println("Math Score: ");
		math = input.nextInt();
		System.out.println("Computer Score: ");
		computer = input.nextInt();
		
		sum = korean + english + math + computer;
		average = sum / 4;
		
		System.out.println("The average score is " + average);
	}
}