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
		
		System.out.println("국어 점수 : ");
		korean = input.nextInt();
		System.out.println("영어 점수 : ");
		english = input.nextInt();
		System.out.println("수학 점수 : ");
		math = input.nextInt();
		System.out.println("컴퓨터 점수 : ");
		computer = input.nextInt();
		
		sum = korean + english + math + computer;
		average = sum / 4;
		
		System.out.println("평균점수는 : " + average + "점 입니다.");
	}
}