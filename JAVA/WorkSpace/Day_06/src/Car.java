
public class Car {
	//Status : Speed, Color, Mileage
	int speed;
	String color;
	int mileage;
	
	//Function : Acceleration, Deceleration, Current state (print)
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
		System.out.println("Current speed : " + speed);
		System.out.println("Color : " + color);
		System.out.println("Mileage : " + mileage);
	}

}
