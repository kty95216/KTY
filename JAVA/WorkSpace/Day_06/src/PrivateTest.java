
public class PrivateTest 
{
	//Status : Speed, Color, Mileage
	private int speed;
	private String color;
	private int mileage;

	//매개변수가 없는 생성자 -> 기본 생성자라고 말함
	//Default constructor
	public PrivateTest()
	{
		System.out.println("Default constructor");
		this.speed = 0;
		this.mileage = 0;
		this.color = "WHITE";
	}
	
	public PrivateTest(int s, String c, int m)
	{
		System.out.println("Constructor that receives three parameters");
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
//	//Function: Acceleration, Deceleration, Current state (print)
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
//		System.out.println("Current Speed : " + speed);
//		System.out.println("Color : " + color);
//		System.out.println("Mileage : " + mileage);
//	}
	public String toString()
	{
		return "Current Speed : " + speed +
				"\nColor : " + color +
				"\nMileage : " + mileage;
	}
}
