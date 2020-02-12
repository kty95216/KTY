
public class Goat extends Animal
{
	public Goat() {}	//Default constructor of Goat
	public Goat(String name)
	{
		this.name = name;
	}
	@Override
	public void bark()
	{
		System.out.println(name + " barks. Meh~~~~~~");
	}
}