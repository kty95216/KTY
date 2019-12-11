
public class StructTest2 
{
	public static void 그림그리기명령어집합(String name) 
	{
		System.out.println("===============");
		System.out.println("내가 그린 그림ㅋㅋㅋ" + name);
		System.out.println("===============");
		System.out.println("내가 그린 그림ㅋㅋㅋ" + name);
		//나중에 다시 사용될 가능성이 높은 코드들에다가 이름을 지어주면 재활용하기 좋음
	}
	public static void main(String[] args) 
	{
		그림그리기명령어집합("구민상");
		System.out.println("구구단");
		그림그리기명령어집합("팔민상");
		System.out.println("로또");
		그림그리기명령어집합("칠민상");
	}
}
