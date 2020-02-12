
public class homework 
{
	public static void main(String[] args)
	{
//		1.
//		Scanner scan = new Scanner(System.in);
//		
//		int num1, num2;
//		String op;
//		
//		System.out.print(Integer 1 : ");
//		num1 = scan.nextInt();
//		System.out.print("Integer 2 : ");
//		num2 = scan.nextInt();
//		System.out.print("Select(+, -, *, /) : ");
//		op = scan.next();
//		
//		switch(op) {
//		case "+":
//			System.out.println(num1 + " + " + num2 + " = " + (num1 + num2));
//			break;
//		case "-":
//			System.out.println(num1 + " - " + num2 + " = " + (num1 - num2));
//			break;
//		case "*":
//			System.out.println(num1 + " * " + num2 + " = " + (num1 * num2));
//			break;
//		case "/":
//			System.out.println(num1 + " / " + num2 + " = " + (num1 / num2));
//			break;
//		}
		
//		2.	
//		int num1 = 0;
//		int num2 = 1;
//		int temp = 0;
//		
//		for (int i = 1; i <= 10; i++) {
//			System.out.print(temp);
//			temp = num1 + num2;
//			num1 = num2;
//			num2 = temp;
//			
//			if (i < 10)
//				System.out.print(", ");
//		}
		
//		3.	
//		Scanner scan = new Scanner(System.in);
//		int num1 = 0;
//		int num2 = 1;
//		int temp = 0;
//		int sum = 0;
//		int what;
//		
//		what = scan.nextInt();
//		
//		for (int i = 1; i < what; i++) {
//			temp = num1 + num2;
//			num1 = num2;
//			num2 = temp;
//			sum += num1;
//		}
//		System.out.println(sum);
		
//		4.	
//		int dan;
//		int i, j;
//		
//		for (j = 1; j < 10; j+=3) {
//			for (i = 1; i <= 9; i++) {
//				for (dan = j; dan <= j+2; dan++) {
//					System.out.print(dan + " * " + i + " = " + dan*i);
//					System.out.print("\t");
//				}
//				System.out.println();
//			}
//			System.out.println();
//		}
		
//		1.	
//		int i, j;
//		for (i = 1; i <= 5; i++) {
//			for (j = 1; j <= 5; j++) {
//				System.out.print((j <= i) ? "*" : " ");
//			}
//			System.out.println();
//		}
		
		
//		2.
//		int i, j;
//		for (i = 1; i <= 5; i++) {
//			for (j = 1; j <= 5; j++) {
//				System.out.print((5 - j >= i) ? " " : "*");
//			}
//			System.out.println();
//		}

		
//		3.
//		int i, j;
//		for (i = 1; i <= 5; i++) {
//			for (j = 1; j <= 5; j++) {
//				System.out.print((j <= 6 - i) ? "*" : " ");
//			}
//			System.out.println();
//		}
		
		
//		4.
//		int i, j;
//		for (i = 1; i <= 5; i++) {
//			for (j = 1; j <= 5; j++) {
//				System.out.print((i <= j) ? "*" : " ");
//			}
//			System.out.println();
//		}
		
		
//		5.
//		int i, j;
//		int k = 0;
//		
//		for (i = 1; i <= 9; i++) {
//			for (j = 0; j < 5; j++) {
//				System.out.print((j <= k) ? "*" : " ");
//			}
//			k = (i < 5) ? (k+=1) : (k-=1);
//			System.out.println();
//		}
		
		
//		6.
//		int i, j;
//		int k = 0;
//		
//		for (i = 1; i <= 9; i++) {
//			for (j = 0; j < 5; j++) {
//				System.out.print((j < 4 - k) ? " " : "*");
//			}
//			k = (i < 5) ? (k+=1) : (k-=1);
//			System.out.println();
//		}
		
		
//		7.
//		int i, j;
//		int k = 0;
//		
//		for (i = 1; i <= 9; i++) {
//			for (j = 0; j < 5; j++) {
//				System.out.print((j < 5 - k) ? "*" : " ");
//			}
//			k = (i < 5) ? (k+=1) : (k-=1);
//			System.out.println();
//		}
		
		
//		8.
//		int i, j;
//		int k = 0;
//		
//		for (i = 1; i <= 9; i++) {
//			for (j = 1; j <= 5; j++) {
//				System.out.print((j <= k) ? " " : "*");
//			}
//			k = (i < 5) ? (k+=1) : (k-=1);
//			System.out.println();
//		}

		
//		9.
//		int i, j;
//		int k = 1;
//		
//		for (i = 1; i <= 7; i++) {
//			for (j = 1; j <= 9; j++) {
//				System.out.print((5 - k >= j || 5 + k <= j) ? "*" : " ");
//			}
//			System.out.println();
//			k = (i < 4) ? (k+=1) : (k-=1);
//		}
		
		
//		10.
//		int i, j;
//		
//		for (i = 1; i <= 5; i++) {
//			for (j = 1; j <= 9; j++) {
//				System.out.print((5 - i >= j || 5 + i <= j) ? " " : "*");
//			}
//			System.out.println();
//		}
		
		
//		11.
//		int i, j;
//		
//		for (i = 5; i > 0; i--) {
//			for (j = 1; j <= 9; j++) {
//				System.out.print((5 - i >= j || 5 + i <= j) ? " " : "*");
//			}
//			System.out.println();
//		}
		
		
//		12.
//		int i, j;
//		int k = 5;
//		
//		for (i = 9; i >= 1; i--) {
//			for (j = 1; j <= 9; j++) {
//				System.out.print((5 - k >= j || 5 + k <= j) ? " " : "*");
//			}
//			System.out.println();
//			k = (i > 5) ? (k-=1) : (k+=1);
//		}
		
		
//		13.
//		int i, j;
//		int k = 3;
//		
//		for (i = 9; i >= 1; i--) {
//			for (j = 1; j <= 9; j++) {
//				System.out.print((k - 3 >= j || k + 3 <= j) ? " " : "*");
//			}
//			System.out.println();
//			k = (i > 5) ? (k+=1) : (k-=1);
//		}
		
		
//		14.
//		int i, j;
//		
//		for (i = 0; i < 5; i++) {
//			for (j = 1; j <= 9; j++) {
//				System.out.print((5 - i == j || 5 + i == j || i == 4) ? "*" : " ");
//			}
//			System.out.println();
//		}
		
		
//		15.
//		int i, j;
//		int k = 2;
//		for (i = 1; i <= 5; i++) {
//			for (j = 1; j <= 5; j++) {
//				System.out.print((3 - k == j || 3 + k == j) ? "*" : " ");
//			}
//			k = (i < 3) ? (k-=1) : (k+=1);
//			System.out.println();
//		}
	}
	
}
