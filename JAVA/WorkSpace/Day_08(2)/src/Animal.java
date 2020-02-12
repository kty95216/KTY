
public class Animal 
{
	protected String name; //public 폴더가 달라도 데이터 교환O , protected 폴더가 다르면 데이터 교환X , private 본인클래스 내에서만 데이터 교환 O
	
	public void bark()
	{
		System.out.println("Animals bark");
	}
	
	public String getName() 
	{
		return name;
	}
	public void setName(String name) 
	{
		this.name = name;
	}
}