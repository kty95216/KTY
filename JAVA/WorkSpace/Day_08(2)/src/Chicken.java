
public class Chicken extends Animal
{
	//치킨객체가 프라이드인지 아닌지를 저장할 변수
	private boolean fried;
	public boolean isFried() 
	{
		return fried;
	}
	public void setFried(boolean fried) 
	{
		this.fried = fried;
	}

	
	public Chicken() {}	//Chicken의 기본생성자
	public Chicken(String name)
	{
		this.name = name;
	}
	@Override
	public void bark()
	{
		System.out.println(name + "가 짖습니다. 꼬끼오!~!~!~!~!");
	}
}