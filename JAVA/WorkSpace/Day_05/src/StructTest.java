class student
{//student라는 새로운 자료형(데이터타입) 만듬
	int age;
	int score;
	String name;
}

public class StructTest 
{
	public static void main(String[] args) 
	{
		//구조체 : 서로 다른 타입의 변수들의 묶음 자료형(데이터타입) -> 사용자 정의 자료형(데이터타입)
		
		student s = new student(); //student타입의 데이터를 생성 (s에는 주소값이 담겨있다.)
		s.age = 10;
		s.score = 100;
		s.name = "학생1";
		System.out.println(s);
		
		System.out.println("나이 : " + s.age);
		System.out.println("점수 : " + s.score);
		System.out.println("이름 : " + s.name);
		//학생한명을 더 만들어서, age, score, name에 각각 어떤 값들을 넣고, 그 값들을 출력해보세요
		student s2 = new student();
		s2.age = 20;
		s2.score = 90;
		s2.name = "학생2";
		
		System.out.println("나이 : " + s2.age);
		System.out.println("점수 : " + s2.score);
		System.out.println("이름 : " + s2.name);
	}
}
