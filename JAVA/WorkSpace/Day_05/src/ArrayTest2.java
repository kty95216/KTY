import java.util.Scanner;

public class ArrayTest2 
{
	public static void main(String[] args) 
	{
		int[] salary = new int[2];
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter the salary of employee 1: ");
		salary[0] = scan.nextInt();
		System.out.print("Enter the salary of employee 2: ");
		salary[1] = scan.nextInt();
		System.out.println("Employee 1's salary is " + salary[0]);
		System.out.println("Employee 2's salary is " + salary[1]);
	}
}