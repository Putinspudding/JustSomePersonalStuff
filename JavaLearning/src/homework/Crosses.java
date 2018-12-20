package homework;
import javafx.application.*;
import javafx.scene.*;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Line;
import javafx.stage.*;
import homework.LinePane;

public class Crosses extends Application{
	@Override
	public void start(Stage primaryStage)
	{
		Scene scene = new Scene(new LinePane(),200,200);
		primaryStage.setTitle("Show Cross");
		primaryStage.setScene(scene);
		primaryStage.show();
	}
	public static void main(String[]args)
	{
		launch(args);
	}
}

class LinePane extends Pane{
	public LinePane() {
		Line line1=new Line(0,100,200,100);
		line1.endXProperty().bind(widthProperty());
		line1.endYProperty().bind(heightProperty().multiply(0.5));
		line1.startYProperty().bind(heightProperty().multiply(0.5));
		line1.setStrokeWidth(5);
		line1.setStroke(Color.RED);
		getChildren().add(line1);
		
		Line line2=new Line(100,0,100,200);
		line2.startXProperty().bind(widthProperty().multiply(0.5));
		line2.endXProperty().bind(widthProperty().multiply(0.5));
		line2.endYProperty().bind(heightProperty());
		line2.setStrokeWidth(5);
		line2.setStroke(Color.RED);
		getChildren().add(line2);
		
		Line line3=new Line(0,0,200,200);
		line3.endXProperty().bind(widthProperty());
		line3.endYProperty().bind(heightProperty());
		line3.setStrokeWidth(5);
		line3.setStroke(Color.RED);
		getChildren().add(line3);
		
		Line line4=new Line(200,0,0,200);
		line4.endYProperty().bind(heightProperty());
		line4.startXProperty().bind(widthProperty());
		line4.setStrokeWidth(5);
		line4.setStroke(Color.RED);
		getChildren().add(line4);
	}
}
