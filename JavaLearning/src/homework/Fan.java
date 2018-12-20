package homework;

public class Fan {
	public static int SLOW = 1;
	public static int MEDIUM = 2;
	public static int FAST = 3;
	private int speed;
	private boolean on;
	private double radius;
	String color;
	
	int getSpeed() {
		return speed;
	}
	boolean getOn() {
		return on;
	}
	double getRadius() {
		return radius;
	}
	String getColor() {
		return color;
	}
	void changeSpeed(int s) {
		speed = s;
	}
	void changeOn() {
		on = !on;
	}
	void changeRadius(double r) {
		radius = r;
	}
	void changeColor(String c) {
		color=c;
	}
	Fan(){
		speed=SLOW;
		on=false;
		radius=5;
		color="blue";
	}
	public String toString(){
		if(on) {
		return speed+" "+color+" "+radius;
		}
		else {
			return "fan is off;"+" "+color+" "+radius;
		}
	}
	public static void main(String[]args)
	{
		Fan fan=new Fan();
		fan.changeOn();
		System.out.println(fan.toString());
	}
}
