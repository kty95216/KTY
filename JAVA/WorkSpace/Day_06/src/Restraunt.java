
public class Restraunt 
{
	private String rice;
	private String side1;
	private String side2;
	private String calory;
	private String soup;
	private int price;
	
	public String getRice() {
		return rice;
	}
	public void setRice(String rice) {
		this/*this.는 멤버변수를 뜻함*/.rice = rice;
	}
	public String getSide1() {
		return side1;
	}
	public void setSide1(String side1) {
		this.side1 = side1;
	}
	public String getSide2() {
		return side2;
	}
	public void setSide2(String side2) {
		this.side2 = side2;
	}
	public String getCalory() {
		return calory;
	}
	public void setCalory(String calory) {
		this.calory = calory;
	}
	public String getSoup() {
		return soup;
	}
	public void setSoup(String soup) {
		this.soup = soup;
	}
	public int getPrice() {
		return price;
	}
	public void setPrice(int price) {
		this.price = price;
	}
	
	public String toString() 
	{
		return "Restraunt [rice=" + rice + ", side1=" + side1 + ", side2=" + side2 + ", calory=" + calory + ", soup="
				+ soup + ", price=" + price + "]";
	}
}