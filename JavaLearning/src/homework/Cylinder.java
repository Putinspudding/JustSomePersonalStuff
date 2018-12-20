package homework;
import java.util.Scanner;

public class Cylinder extends Circle{
	double height;
	
	Cylinder(double r,double h) {
		radius=r;
		height=h;
		}
	
	double getHeight() {
		return height;
	}
	
	double getVol() {
		return this.getArea()*height;
	}
	public static void main(String []args) {
		Scanner input=new Scanner(System.in);
		double r=input.nextDouble();
		double h=input.nextDouble();
		Cylinder a=new Cylinder(r,h);
		System.out.println(a.getHeight());
		System.out.println(a.getVol());
	}
}
