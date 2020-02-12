
public class Rectangle extends Shape
{
	private int width;
	private int height;
	
	@Override
	public void draw() 
	{
		System.out.println("Draw a rectangle");
	}
	
	public int getWidth() 
	{
		return width;
	}
	public void setWidth(int width) 
	{
		this.width = width;
	}
	public int getHeight() 
	{
		return height;
	}
	public void setHeight(int height) 
	{
		this.height = height;
	}
}
