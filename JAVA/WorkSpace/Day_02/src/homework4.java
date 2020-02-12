import java.util.Scanner;

public class homework4 
{
	public static void main(String[] args) 
	{
		Scanner input = new Scanner(System.in);
		
		int score; //사용자로부터 점수 입력받을 변수
		String result; //상항연산 조건검사를 통해 산출한 학점을 저장할 변수
		
		//사용자한테 점수 입력하라고 안내메세지 출력해주고
		//사용자가 숫자를 입력하면 준비해둔 score변수에 담읍시다.
		System.out.println("Enter your score: ");
		score = input.nextInt();
		
		result = score >= 90 ? "A" : 
					(score >= 80 ? "B" : 
						(score >= 70 ? "C" : 
							(score >= 60 ? "D" : "fool")));
		System.out.println("Your grade is " + result);
	}
}
