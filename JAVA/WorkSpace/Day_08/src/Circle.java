
public class Circle extends Shape
{
	private int radius;

	@Override
	public void draw() 
	{
		System.out.println("원을 그립니다 똥글똥글");
	}

	public int getRadius() 
	{
		return radius;
	}
	public void setRadius(int radius) 
	{
		this.radius = radius;
	}
}
