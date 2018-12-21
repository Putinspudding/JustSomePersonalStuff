package homework;
import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;
public class GUI extends Application{
	public static GridPane pane=new GridPane();
	public static TextField tf= new TextField();
	@Override
	public void start(Stage primaryStage) throws Exception {
		Button bt=new Button("确认");
		Button btOpen= new Button("新窗口");
		HandlerClass hanlder1=new HandlerClass();
		bt.setOnAction(hanlder1);
		pane.setAlignment(Pos.CENTER);
		pane.setPadding(new Insets(60,60,60,60));
		pane.setHgap(6);
		pane.setVgap(6);
		
		pane.add(new Label("请输入圆的半径："),0,0);
		pane.add(tf,1,0);
		pane.add(bt,1,2);
		pane.add(btOpen, 2, 2);
		btOpen.setOnAction(new EventHandler<ActionEvent>(){
			public void handle(ActionEvent event){
				Stage nextStage=new Stage();
				GridPane pane1=new GridPane();
				pane1.setAlignment(Pos.CENTER);
				pane1.setPadding(new Insets(60,60,60,60));
				pane1.setHgap(6);
				pane1.setVgap(6);
				Label l1=new Label();
				Label l2=new Label();
				int r=Integer.parseInt(GUI.tf.getText());
				if (r>0) {
					Circle c= new Circle(r);
					l1.setText("周长是："+c.getPerimeter());
					l2.setText("面积是："+c.getArea());
					pane1.add(l1,1,0);
					pane1.add(l2,1,1);
				}
				else
					pane1.add(new Label("请输入大于零的半径值!"),1,1);
				Scene scene1=new Scene(pane1);
				nextStage.setScene(scene1);
				nextStage.show();
			}	
		});
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
		Label l1=new Label();
		Label l2=new Label();
		try{
		GUI.pane.getChildren().remove(4);
		GUI.pane.getChildren().remove(4);
		}
		finally{
		int r=Integer.parseInt(GUI.tf.getText());
		if (r>0) {
			Circle c= new Circle(r);
			l1.setText("周长是："+c.getPerimeter());
			l2.setText("面积是："+c.getArea());
			GUI.pane.add(l1,1,3);
			GUI.pane.add(l2,1,4);

		}
		else
			GUI.pane.add(new Label("请输入大于零的半径值!"),1,3);
		}
	}
}
