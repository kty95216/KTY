
public class PrivateTest 
{
	//상태 : 속도, 색상, 주행거리
	private int speed;
	private String color;
	private int mileage;

	//매개변수가 없는 생성자 -> 기본 생성자라고 말함
	public PrivateTest()
	{
		System.out.println("기본 생성자 입니다.");
		this.speed = 0;
		this.mileage = 0;
		this.color = "WHITE";
	}
	
	public PrivateTest(int s, String c, int m)
	{
		System.out.println("매개변수 3개 받는 생성자입니다.");
		this.speed = s;
		this.mileage = m;
		this.color = c;
	}
		
	//정수값 하나를 매개변수로 받아서 speed멤버변수에 값을 넣어주는 메소드
		
//	public void setSpeed(int s)
//	{
//		speed = s;
//	}
//	
//	//speed값을 갖다주는 메소드
//		
//	public int/*반환유형*/ getSpeed()
//	{
//		return speed;	//반환유형이 void가 아니면 반드시 반환받는것이 적어도 한개는 있어야한다.그래서 반환하는 명령어 return사용
//	}
//		
//	public int getMileage() 
//	{
//		return mileage;
//	}
//		
//	public String getColor()
//	{
//		return color;
//	}
//		
//	public void setMileage(int m)
//	{
//		mileage = m;
//	}
//		
//	public void setColor(String c)
//	{
//		color = c;
//	}
//		
//	//기능 : 가속, 감속, 현재상태 출력
//	public void speedUp(int s)
//	{
//		speed += s;
//	}
//	public void speedDown(int s) 
//	{
//		speed -= s;
//	}
//	public void print()
//	{
//		System.out.println("현재속도 : " + speed);
//		System.out.println("색     상 : " + color);
//		System.out.println("주행거리 : " + mileage);
//	}
	public String toString()
	{
		return "현재속도 : " + speed +
				"\n색    상 : " + color +
				"\n주행거리 : " + mileage;
	}
}
