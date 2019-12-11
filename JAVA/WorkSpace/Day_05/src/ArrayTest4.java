import java.util.Scanner;

public class ArrayTest4 
{
	public static void main(String[] args) 
	{
		Scanner scan = new Scanner(System.in);
		int student = 0;
		double total = 0;
		double avg = 0;
		
		System.out.print("학생 수를 입력하세요 : ");
		student = scan.nextInt();
		
		double[] studentnumber = new double[student];
		
		for(int i=0 ; i < student ; i++)
		{
			System.out.print("학생" + (i+1) + "의  점수 입력 : ");
			studentnumber[i] = scan.nextDouble();
			total += studentnumber[i];
		}
		
		avg = total / student;
		System.out.println(student + "명의 평균점수 : " + avg);
	}
}