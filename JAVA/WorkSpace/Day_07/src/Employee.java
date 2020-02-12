
public class Employee 
{
	private String name;
	private double salary;
	private static int count = 0;
	
	public Employee(String name, double salary)
	{
		this.name = name;
		this.salary = salary;
		count ++;
	}
	
	public Employee()
	{
		// TODO Auto-generated constructor stub
		System.out.println("Create object");
		name = "No Name";
		salary = 300;
		count ++;
	}

	@Override
	public String toString()
	{
		return "Employee [name=" + name + ", salary=" + salary + "]";
		//toString은 우리가 만들지 않아도 원래 존재하는 친구임...
		//해당 객체가 문자열 화 될 때 어떤모양의 문자열로 바뀔지를 결정하는 기능.
		//이미 존재하지만 똑같은 이름으로 toString을 다시 만들어주면
		//해당 객체가 문자열화 될 때 우리가 정의한 내용에 맞게 문자열화 되는기능.
	}
	
	protected void finalize()	//finalize도 원래 존재하는 함수 , 객체가 소멸되기 직전에 호출되는 메소드 , 우리가 똑같은 이름으로 다시 정의하면 해당 객체가 소멸될 때 우리가 정의한 함수의 내용을 실행함
	{
		count--;
	}
	
	public static int getCount() 
	{
		return count;
	}

	public static void setCount(int count) 
	{
		Employee.count = count;
	}

	public String getName() 
	{
		return name;
	}

	public void setName(String name) 
	{
		this.name = name;
	}

	public double getSalary() 
	{
		return salary;
	}

	public void setSalary(double salary) 
	{
		this.salary = salary;
	}
}
