
public class AnimalTest 
{
	public static void main(String[] args) 
	{
		Animal[] animals = new Animal[3];
		animals[0] = new Goat("Baby goat");
		animals[1] = new Cow("Bull");
		animals[2] = new Chicken("Hosik");
		
		//부모클래스의 타입으로 자식객체를 참조했을 때는 부모클래스에 존재하는 멤버변수와 멤버함수에만 접근이 가능함. 자식영역에만 존재하는 멤버에는 접근 불가능
		//animals[2].setFried(true);
		
		//객체 형변환
		//자식클래스로 형변환을 통해 자식에만 존재하는 멤버에 잠시 접근이 가능
        //((Chicken)animals[2]).setFried(true);
		
		//자식클래스와 자식클래스는 cast 불가능!!! , 맞지않는 타입으로 형변환을 하려고하면 런타임에러가 발생한다.
		//((Chicken)animals[0]).setFried(true);
		
		if(animals[0] instanceof Chicken)
		{
			System.out.println("animals[0] is Chicken");
		}
		if(animals[2] instanceof Chicken)
		{
			System.out.println("animals[2] is Chicken");
		}
		if(animals[2] instanceof Chicken)
		{
			((Chicken) animals[2]).setFried(true);;
		}
		for(Animal a : animals)
		{
			a.bark();
		}
	}
}