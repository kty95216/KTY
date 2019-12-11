class Date 
{
	private int year;
	private String month;
	private int day;
	
	public Date()	//기본 생성자
	{
		month = "1월";
		day = 1;
		year = 2009;
	}
	
	public Date(int year, String month, int day)	//생성자
	{
		setDate(year, month, day);
	}
	
	public Date(int year)	//생성자
	{
		setDate(year, "1월", 1);
	}
	
	public void setDate(int year, String month, int day)	//this는 현재 객체를 가리킨다.
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
		Date date1 = new Date(2009,"3월",2);	//2009.3.2
		Date date2 = new Date(2010);		//2010.1.1
		Date date3 = new Date();			//2009.1.1
	}
}