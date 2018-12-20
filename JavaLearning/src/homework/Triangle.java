package homework;
import java.util.*;
public class Triangle {
	int a,b,c;
	Triangle(){
		a=0;
		b=0;
		c=0;
	}
	Triangle(int x,int y,int z){
		if(x+y>z&&Math.abs(x-y)<z) {
			a = x;
			b = y;
			c = z;
		}
		else{
			throw new IllegalArgumentException("Unable to create a triangle");
		}
	}
	String getTriangleType(){
		if(this.a==this.b||this.b==this.c||this.c==this.a) {
			if(this.a==this.b&&this.b==this.c)
			{
				return "Equilateral triangle";
			}
			return "Isosceles triangle";
		}
		else if(Math.pow(a, 2)+Math.pow(b, 2)==Math.pow(c, 2)||Math.pow(c, 2)+Math.pow(b, 2)==Math.pow(a, 2)||Math.pow(a, 2)+Math.pow(c, 2)==Math.pow(b, 2)) {
			return "Right triangle";
		}
		else
			return "Normal triangle";
	}
	public static void main(String []args) {
		Triangle tri = new Triangle(6,5,5);
		System.out.println(tri.getTriangleType());
	}
}
