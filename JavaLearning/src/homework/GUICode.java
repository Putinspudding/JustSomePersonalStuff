package homework;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;
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
public class GUICode extends Application{
	public static GridPane pane=new GridPane();
	public static TextField tf= new TextField();
	public static TextField text=new TextField();
	Scanner input;
	Scanner cpyInput;
	PrintWriter cpyOutput;
	PrintWriter output;
	@Override
	public void start(Stage primaryStage) throws Exception {
		Button bt=new Button("加密");
		Button btCpy= new Button("解密");
		pane.setAlignment(Pos.CENTER);
		pane.setPadding(new Insets(60,60,60,60));
		pane.setHgap(6);
		pane.setVgap(6);
		
		pane.add(new Label("请输入文件名（除扩展名）"), 0, 0);
		pane.add(new Label("请选择加密/解密"),0,1);
		pane.add(text, 0, 2);
		pane.add(tf,0,3);
		pane.add(bt,0,4);
		pane.add(btCpy, 2, 4);
		
		String target="";
		String end="";	
		StringBuffer rakey=new StringBuffer();

		bt.setOnAction(new EventHandler<ActionEvent>() {
			public void handle(ActionEvent e) {
					String fileName=text.getText();
					File file = new File(fileName+".txt");
					try {
						input = new Scanner(file);
					} catch (FileNotFoundException e1) {
						// TODO Auto-generated catch block
						text.setText("文件不存在！");
					}
				char []arr=judge(target,input).toCharArray();
				StringBuffer rakey=new StringBuffer();
				for(int i=0;i<arr.length;i++) {
					int ra=(int) (Math.random()*9)+1;
					if(ra%2==0) {
						arr[i]=(char) (arr[i]+ra);
					}
					else {
						arr[i]=(char) (arr[i]-ra);
					}
					rakey.append(ra);
				}
				System.out.println(arr);
				try {
					output=new PrintWriter(fileName+"-enc.txt");
				} catch (FileNotFoundException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
				output.print(arr);
				output.close();
				String temp=rakey.toString();
				tf.getText();
				tf.setText(temp);
				}
		});
		btCpy.setOnAction(new EventHandler<ActionEvent>(){
			public void handle(ActionEvent event){
				String fileName=text.getText();
				File file=new File(fileName+"-enc.txt");
				try {
					cpyInput=new Scanner(file);
				} catch (FileNotFoundException e) {
					// TODO Auto-generated catch block
					text.setText("文件不存在！");
				}
				char []array=judge(end,cpyInput).toCharArray();
				String temp=tf.getText();
				String[] keys=temp.split("");
				for(int i=0;i<keys.length;i++) {
					if(Integer.parseInt(keys[i])%2==0) {
						array[i]=(char) (array[i]-Integer.parseInt(keys[i]));
					}
					else
						array[i]=(char) (array[i]+Integer.parseInt(keys[i]));
				}
				try {
					cpyOutput= new PrintWriter(fileName+"-ori.txt");
				} catch (FileNotFoundException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				cpyOutput.print(array);
				cpyOutput.close();
				System.out.println(array);
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
	String judge(String str,Scanner inp) {
		while(inp.hasNext()) {
			String piece=inp.nextLine();
			str=str+piece+" ";
		}
		return str;
	}
}

