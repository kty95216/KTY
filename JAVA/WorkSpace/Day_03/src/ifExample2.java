import java.util.Scanner;

public class ifExample2 
{
	public static void main(String[] args) 
	{
		Scanner input = new Scanner(System.in);
		double score;
		
		System.out.print("Enter your score: ");
		score = input.nextDouble();
		
		if(score >= 90)
			System.out.println("A");
		else if(score >= 80)
			System.out.println("B");
		else if(score >= 70)
			System.out.println("C");
		else if(score >= 60)
			System.out.println("D");
		else
			System.out.println("Fool");
			
	}
}
