
public class Car {
	//상태 : 속도, 색상, 주행거리
	int speed;
	String color;
	int mileage;
	
	//기능 : 가속, 감속, 현재상태 출력
	public void speedUp(int s)
	{
		speed += s;
	}
	public void speedDown(int s) 
	{
		speed -= s;
	}
	public void print()
	{
		System.out.println("현재속도 : " + speed);
		System.out.println("색     상 : " + color);
		System.out.println("주행거리 : " + mileage);
	}

}
