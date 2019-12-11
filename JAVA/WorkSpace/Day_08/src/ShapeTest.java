
public class ShapeTest 
{
	public static void main(String[] args) 
	{
		//Rectange이 Shape를 상속받았기 때문에
		//Shape의 참조변수로 Rectangle 객체를 참조 가능함.
		Shape s = new Rectangle();
		
		//Rectangle이 Shape를 상속받았고
		//Shape가 print()메소드를 정의했으므로 당연 호출가능
		s.print();
		
		//Rectangle에는 setWidth(int)메소드가 존재하지만
		//부모클래스의 참조변수로 참조했을 때는 Shape에도 존재하는
		//멤버에만 접근가능함
		//s.setWidth(10);
		
		//draw는 Shape가 정의했으므로 접근 가능하고
		//Rectangle이 오버라이딩했으므로 실제 실행되는 함수는 Rectangle의 draw(동적바인딩)
		s.draw();
		
		
		
		Shape[] shape = new Shape[4];	//Shape[] : 데이터타입의 배열
		shape[0] = new Rectangle();
		shape[1] = new Circle();
		shape[2] = new Triangle();
		shape[3] = new Cylinder();
		
		for(int i = 0 ; i < shape.length ; i++)
		{
			shape[i].draw();
		}
	}
}
