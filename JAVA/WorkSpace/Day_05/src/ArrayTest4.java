import java.util.Scanner;

public class ArrayTest4 
{
	public static void main(String[] args) 
	{
		Scanner scan = new Scanner(System.in);
		int student = 0;
		double total = 0;
		double avg = 0;
		
		System.out.print("Enter the number of students : ");
		student = scan.nextInt();
		
		double[] studentnumber = new double[student];
		
		for(int i=0 ; i < student ; i++)
		{
			System.out.print("Enter the score for student" + (i+1) + " : ");
			studentnumber[i] = scan.nextDouble();
			total += studentnumber[i];
		}
		
		avg = total / student;
		System.out.println("Average score of " + student + " people : " + avg);
	}
}