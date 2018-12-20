package homework;

import java.util.*;

public class MyPoint {
	double x;
	double y;
	
	double getX() {
		return x;
	}
	double getsY() {
		return y;
	}
	MyPoint()
	{
		x=0;
		y=0;
	}
	MyPoint(double X, double Y){
		x = X;
		y = Y;
	}
	double distance(MyPoint point)
	{
		double sqx = Math.pow(this.x-point.x,2);
		double sqy = Math.pow(this.y-point.y,2);
		double sqz = Math.pow((sqx+sqy), 0.5);
		return sqz;
	}
	double distance(double X,double Y) 
	{
		double sqx = Math.pow(this.x-X,2);
		double sqy = Math.pow(this.y-Y,2);
		double sqz = Math.pow((sqx+sqy), 0.5);
		return sqz;
	}
	
	public static void main(String []args)
	{
		MyPoint my=new MyPoint(3,4);
		MyPoint point=new MyPoint(0,0);
		System.out.println(my.distance(point));
	}
}
