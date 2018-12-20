package homework;
import java.util.*;

public class Circle {
	double radius;
	
	Circle(){
		radius = 0;
	}
	
	Circle(double r){
		radius = r;
	}
	
	double getRadius() {
		return radius;
	}
	
	double getPerimeter() {
		return 2*Math.PI*radius;
	}
	
	double getArea() {
		return Math.PI*Math.pow(radius, 2);
	}
	
	public static void main(String []args) {
		Scanner input=new Scanner(System.in);
		double r=input.nextDouble();
		Circle a=new Circle(r);
		System.out.println(a.getRadius());
		System.out.println(a.getPerimeter());
		System.out.println(a.getArea());
	}
}
