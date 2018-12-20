package homework;

import java.util.*;

public class ArraySumMain{
	public static void main(String []args) {
		int i=0;
		ArrayList<Integer> list=new ArrayList<>();
		Scanner input=new Scanner(System.in);
		System.out.println("Please input 5 integers");
		for(i=0;i<5;i++) {
			list.add(input.nextInt());
		}
		ArraySum.sum(list);
		System.out.println(ArraySum.summary);
	}
}
class ArraySum {
	static int summary;
	public static void sum(ArrayList<Integer> list) 
	{
		int i=0;
		int sum=0;
		for(i=0;i<5;i++)
		{
			sum+=list.get(i);
		}
		summary=sum;
	}
}

