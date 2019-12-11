
public class Rectangle extends Shape
{
	private int width;
	private int height;
	
	@Override
	public void draw() 
	{
		System.out.println("사각형을 그립니다 슥슥삭삭");
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
