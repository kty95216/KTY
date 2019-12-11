
public class CarTest 
{
	public static void main(String[] args) 
	{
		SportsCar sCar = new SportsCar();
		
		sCar.color = "RED";
		sCar.setGear(3);
		sCar.setSpeed(200);
		sCar.setTurbo(true);
		
		System.out.println(sCar.color);
		System.out.println(sCar.gear);
		System.out.println(sCar.speed);
		System.out.println(sCar.turbo);
	}
}