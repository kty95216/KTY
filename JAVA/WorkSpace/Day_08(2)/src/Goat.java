
public class Goat extends Animal
{
	public Goat() {}	//Goat의 기본생성자
	public Goat(String name)
	{
		this.name = name;
	}
	@Override
	public void bark()
	{
		System.out.println(name + "가 짖습니다. 음메~~~~~");
	}
}