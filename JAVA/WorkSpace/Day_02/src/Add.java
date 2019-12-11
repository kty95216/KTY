//두수의 합을 계산하는 애플리케이션
/*
public class Add 
{
	public static void main(String args[])
	{
		int x;
		int y;
		int sum;
		
		x = 5200;
		y = 3800;
		sum = x + y;
		
		System.out.println(sum);
	}
}
*/

/*
// 사용자가 입력한 두 개의 숫자를 더해서 출력한다.
import java.util.Scanner; //Scanner 클래스 포함

public class Add
{
	// 메인 메소드에서부터 실행이 시작된다.
	public static void main(String args[])
	{
		// 사용자로부터 입력을 받기위해 Scanner를 생성한다.
		Scanner input = new Scanner(System.in);
		
		int x; // 첫 번째 숫자 저장
		int y; // 두 번째 숫자 저장
		int sum; // 합을 저장
		
		System.out.print("첫번째 숫자를 입력하시오: "); // 입력 안내 출력
		x = input.nextInt(); // 사용자로부터 첫 번째 숫자를 읽는다.
		
		System.out.print("두번째 숫자를 입력하시오: "); // 입력 안내 출력
		y = input.nextInt(); // 사용자로부터 두 번째 숫자를 읽는다.
		
		sum = x + y; // 두 개의 숫자를 더한다.
		
		System.out.println(sum); // 합을 출력한다.
	}
}
*/

/*
import java.util.Scanner;

public class Add
{
	public static void main(String args[])
	{
		Scanner input = new Scanner(System.in);
		
		int x;
		int y;
		int sum;
		
		System.out.print("x의 숫자를 입력하시오 : ");
		x = input.nextInt();
		
		System.out.print("y의 숫자를 입력하시오 : ");
		y = input.nextInt();
		
		sum = x + y;
		
		System.out.println("결과:");
		System.out.printf("x = %d\n",x);
		System.out.printf("y = %d\n",y);
		System.out.printf("x + y = %d 입니다.",sum);			
	}
}
*/