public class Car 
{
	private int speed;
	private int mileage;
	private String color;
	
	//Vehicle serial number
	private int id;
	
	//실체화된 Car 객체의 개수를 위한 정적 변수
	private static int numberOfCars;
	
	public static int getNumberOfCars() 
	{
		//정적메소드의 활용 용도
		//1. 정적변수에 대한 게터 세터
		return numberOfCars;
	}
	
	//의미를 갖는 숫자 : 심볼릭 ★상수★ , int 형태의 심볼릭 상수의 이름은 관례적으로 대문자 사용
	private static final int INCREASE_AMOUNT = 10;	//final : 모든프로그램이 끝날때 까지 값이 변하지않음
	
	public Car()
	{
		//자동차의 개수를 증가하고 id번호를 할당한다.
		id = ++numberOfCars;
	}
	
	public void speedUp()
	{
		//항상 모든 자동차는 가속할 때는 10만큼씩 증가해야됨
		//10이라는 숫자는 그냥 숫자로서의 10이기도 하지만
		//자동차의 속도증가량의 의미를 갖고있음
		speed += INCREASE_AMOUNT;
	}
	
	@Override
	public String toString() 
	{
		return "Car [speed=" + speed + ", mileage=" + mileage + ", color=" + color + ", id=" + id + "]";
	}

	public int getSpeed() 
	{
		return speed;
	}

	public void setSpeed(int speed) 
	{
		this.speed = speed;
	}

	public int getMileage() 
	{
		return mileage;
	}

	public void setMileage(int mileage) 
	{
		this.mileage = mileage;
	}

	public String getColor() 
	{
		return color;
	}

	public void setColor(String color) 
	{
		this.color = color;
	}

	public int getId() 
	{
		return id;
	}

	public void setId(int id) 
	{
		this.id = id;
	}	
}