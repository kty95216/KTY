class Parent
{
	int data = 100;
	public Parent()
	{
		System.out.println("Default constructor of Parent");
	}
	public void print()
	{
		System.out.println("Parent");
	}
}

class Child extends Parent
{
	int data = 200;
	public Child()
	{
//		super();이 코드가 생략 되어있는것 , 너무 많이 사용되어서 생략
		System.out.println("Default constructor of Child");
	}
	public void print()
	{
		int data = 300;
		super.print();  //부모클래스(Parent클래스)의 print()호출
		System.out.println("Child");
		System.out.println(data);
		System.out.println("this.data : " + this.data);
		System.out.println("super.data : " + super.data); //super : 슈퍼클래스 , 부모클래스
	}
}

public class ParentTest 
{
	public static void main(String[] args) 
	{
		Child c = new Child();
		c.print();
	}
}
