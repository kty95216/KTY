import java.util.Scanner;

public class ifExample2 
{
	public static void main(String[] args) 
	{
		Scanner input = new Scanner(System.in);
		double score;
		
		System.out.print("점수를 입력 하세요 : ");
		score = input.nextDouble();
		
		if(score >= 90)
			System.out.println("A등급");
		else if(score >= 80)
			System.out.println("B등급");
		else if(score >= 70)
			System.out.println("C등급");
		else if(score >= 60)
			System.out.println("D등급");
		else
			System.out.println("바보입니다.");
			
	}
}
