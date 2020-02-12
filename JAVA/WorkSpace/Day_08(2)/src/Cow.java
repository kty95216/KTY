
public class Cow extends Animal
{
	public Cow() {}		//Default constructor of Cow
	public Cow(String name)
	{
		this.name = name;
	}
	@Override
	public void bark() 
	{
		System.out.println(name + " barks. Moo~~~~~");
	}
}