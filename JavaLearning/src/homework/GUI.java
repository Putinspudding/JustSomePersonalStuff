package homework;
import javafx.application.Application;
import javafx.geometry.*;
import javafx.scene.*;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.*;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
public class GUI extends Application{
	public static GridPane pane=new GridPane();
	public static TextField tf= new TextField();
	@Override
	public void start(Stage primaryStage) throws Exception {
		Button bt=new Button("确认");
		HandlerClass hanlder1=new HandlerClass();
		bt.setOnAction(hanlder1);
		pane.setAlignment(Pos.CENTER);
		pane.setPadding(new Insets(40,40,40,40));
		pane.setHgap(6);
		pane.setVgap(6);
		
		pane.add(new Label("请输入圆的半径："),0,0);
		pane.add(tf,1,0);
		pane.add(bt,1,2);
		Scene scene = new Scene(pane);
		primaryStage.setScene(scene);
		primaryStage.show();
	}
	public static void main(String [] args)
	{
		launch(args);
	}

}

class HandlerClass implements EventHandler<ActionEvent>{
	@Override
	public void handle(ActionEvent e) {
		int r=Integer.parseInt(GUI.tf.getText());
		if (r>0) {
			Circle c= new Circle(r);
			Label l1=new Label("周长是："+c.getPerimeter());
			Label l2=new Label("面积是："+c.getArea());
			GUI.pane.add(l1,1,3);
			GUI.pane.add(l2,1,4);
		}
		else
			GUI.pane.add(new Label("请输入大于零的半径值!"),1,3);
	}

}
