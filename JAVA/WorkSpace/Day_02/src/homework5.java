import java.util.Scanner;

public class homework5 
{
	public static void main(String[] args) 
	{
		Scanner input = new Scanner(System.in);
		
		int year;	//연도 담을 변수
		char isYoon; //윤년 , 평년 인지를 담을 char변수
		
		System.out.println("Enter year: ");
		year = input.nextInt();
		
		isYoon = ( (year % 4 == 0) && (year % 100 != 0) ) || (year % 400 == 0) ? 'L' : 'N';
		System.out.println(year + " years is " + isYoon + " year");
		
		
	}
}
