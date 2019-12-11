
public class Cow extends Animal
{
	public Cow() {}		//Cow의 기본생성자
	public Cow(String name)
	{
		this.name = name;
	}
	@Override
	public void bark() 
	{
		System.out.println(name + "이가 짖습니다. 음머~~~~");
	}
}