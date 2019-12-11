
public class ArrayTest5
{
	public static void main(String[] args) 
	{
		int[] numbers = new int[5];
		for(int i = 0; i<numbers.length; i++)
		{
			numbers[i] = (int) (Math.random()*1000);
		}
		for (int value : numbers)
		{
			System.out.println(value);
		}
	}
}
