class Date 
{
	private int year;
	private String month;
	private int day;
	
	public Date()	//Default constructor
	{
		month = "January";
		day = 1;
		year = 2009;
	}
	
	public Date(int year, String month, int day)	//Constructor
	{
		setDate(year, month, day);
	}
	
	public Date(int year)	//Constructor
	{
		setDate(year, "January", 1);
	}
	
	public void setDate(int year, String month, int day)	//"This" points to the current object.
	{
		this.month = month;
		this.day = day;
		this.year = year;
	}
}
public class DateTest 
{
	public static void main(String[] args)
	{
		Date date1 = new Date(2009,"March",2);	//2009.3.2
		Date date2 = new Date(2010);		//2010.1.1
		Date date3 = new Date();			//2009.1.1
	}
}