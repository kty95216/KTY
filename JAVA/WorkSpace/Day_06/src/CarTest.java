
public class CarTest 
{
	public static void main(String[] args) 
	{//메인함수 : 하나의 프로젝트에서 키(key), 시작이 되는 부분
		Car abbacha = new Car(); //Car타입의 객체 abbacha생성  //new연산자는 왼쪽 Car클래스(설계도)를 보고 객체를 만드는 연산자이다.
		Car ummacha = new Car(); //Car타입의 객체 ummacha생성
		
		abbacha.speed = 100;
		abbacha.color = "PINK";
		abbacha.mileage = 30000;
		
		ummacha.speed = 200;
		ummacha.color = "BLACK";
		ummacha.mileage = 50000;
		
		abbacha.print();	//abbacha의 주소값을 참조해서 만들어놓은 객체(완성품)의 print()를 찾아가서 실행 절대로!!! 클래스(설계도)를 찾아가지 않음.
		System.out.println("==============");
		ummacha.print();
		
		abbacha.speedUp(20);
		abbacha.speedDown(40);
		
		System.out.println("==============");
		abbacha.print();
		System.out.println("==============");
		ummacha.print();
		
	}
}
