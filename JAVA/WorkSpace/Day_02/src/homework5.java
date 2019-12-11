import java.util.Scanner;

public class homework5 
{
	public static void main(String[] args) 
	{
		Scanner input = new Scanner(System.in);
		
		int year;	//연도 담을 변수
		char isYoon; //윤년 , 평년 인지를 담을 char변수
		
		System.out.println("연도를 입력해봐 : ");
		year = input.nextInt();
		
		isYoon = ( (year % 4 == 0) && (year % 100 != 0) ) || (year % 400 == 0) ? '윤' : '평';
		System.out.println(year + "년은" + isYoon + "년 입니다.");
		
		
	}
}
