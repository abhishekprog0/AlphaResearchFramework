// Java program to demonstrate working of Robot
// class. This program is for Windoes. It opens
// notepad and types a message.
import java.awt.*;
import java.awt.Robot;
import java.awt.event.KeyEvent;
import java.io.*;
import java.util.*;

import java.awt.event.InputEvent;
import java.awt.AWTException;
import java.awt.HeadlessException;
import java.awt.Robot;
import java.awt.Toolkit;
import java.awt.datatransfer.Clipboard;
import java.awt.datatransfer.DataFlavor;
import java.awt.datatransfer.StringSelection;
import java.awt.datatransfer.UnsupportedFlavorException;
import java.awt.event.KeyEvent;
import java.io.IOException;
 

class SuperRobot extends Robot {
    public SuperRobot() throws Exception {
    super();
}
    public void typeKey(int keyCode)throws AWTException {
        keyPress(keyCode);
        delay(20);
        keyRelease(keyCode);
    }
}



public class robo_simulate
{
    public static void executeCommand(Robot robot, int code) throws AWTException, IOException
    {
        try{
            robot.keyPress(KeyEvent.VK_META);
            Thread.sleep(10);
            robot.keyPress(code);
            Thread.sleep(10);
            robot.keyRelease(code);
            Thread.sleep(10);
            robot.keyRelease(KeyEvent.VK_META);
        }
        catch(Exception ex)
        {
            System.out.println("Oh No");
        }

    }
    public static void copy(String text)
    {
        Clipboard clipboard = getSystemClipboard();

        clipboard.setContents(new StringSelection(text), null);
    }

    private static Clipboard getSystemClipboard()
    {
        Toolkit defaultToolkit = Toolkit.getDefaultToolkit();
        Clipboard systemClipboard = defaultToolkit.getSystemClipboard();

        return systemClipboard;
    }

    public static void paste(Robot robot) throws AWTException, IOException
    {
        try{
            executeCommand(robot, KeyEvent.VK_V);
        }
        catch(Exception ex)
        {

        }
    }

    public static void select_all(Robot robot) throws AWTException, IOException
    {
        try{
            executeCommand(robot, KeyEvent.VK_A);
        }
        catch(Exception ex)
        {
            
        }
    }

    public static void close_tab(Robot robot) throws AWTException, IOException
    {
        try{
            executeCommand(robot, KeyEvent.VK_W);
        }
        catch(Exception ex)
        {
            
        }
    }

    public static void new_tab(Robot robot) throws AWTException
    {
        try{
            executeCommand(robot, KeyEvent.VK_T);
        }
        catch(Exception ex)
        {
            
        }
    }

    public static void change_tab(Robot robot) throws AWTException, IOException
    {
        try{
            robot.keyPress(KeyEvent.VK_CONTROL);
            Thread.sleep(30);
            robot.keyPress(KeyEvent.VK_TAB);
            Thread.sleep(30);
            robot.keyRelease(KeyEvent.VK_TAB);
            Thread.sleep(30);
            robot.keyRelease(KeyEvent.VK_CONTROL);
            
        }
        catch(Exception ex)
        {

        }
    }

    public static void click(Robot robot, int x, int y) throws AWTException
    {
        int mask = InputEvent.BUTTON1_DOWN_MASK;
        robot.mouseMove(x, y);           
        robot.mousePress(mask);     
        robot.mouseRelease(mask);
    }

    public static void main(String[] args) throws IOException
    {
        try
        {
            String content = new Scanner(new File("alphas_nomdf.txt")).useDelimiter("\\Z").next();
            String[] data = content.split("@@");
            SuperRobot robot = new SuperRobot();
            String url = "https://websim.worldquantchallenge.com/simulate";
            int count = 1;
            int TAB_LIMIT = 40;
            Thread.sleep(10000);

            for(String x:data)
            {
                System.out.println("Running:\n"+x);
                
                //open new tab
                new_tab(robot);
                Thread.sleep(300);

                //copy url
                copy(url);
                Thread.sleep(300);

                //paste url
                paste(robot);
                Thread.sleep(300);

                //press enter
                robot.typeKey(KeyEvent.VK_ENTER);

                //wait 5 secs
                Thread.sleep(13000);

                //click on textbox
                click(robot, 109, 282);
                Thread.sleep(300);

                //select all
                //select_all(robot);
                //Thread.sleep(300);

                //copy to clipboard
                copy(x);
                Thread.sleep(300);

                //paste to textbox
                paste(robot);
                Thread.sleep(300);

                //click to submit

                for(int l = 330; l < 500; l += 15)
                {
                    click(robot, 476, l);
                    Thread.sleep(50);
                }
                
                Thread.sleep(300);
                /*
                if(++count % TAB_LIMIT == 0)
                {
                    Thread.sleep((TAB_LIMIT/8)*60*1000);
                    change_tab(robot);
                    for(int i=0;i<TAB_LIMIT-1;i++)
                    {
                        Thread.sleep(500);
                        close_tab(robot);
                    }
                }*/
                //Thread.sleep(2000);
                if(count % 4 == 0)
                {
                    Thread.sleep(100000);
                    //submit alpha
                    change_tab(robot);
                    Thread.sleep(500);
                    for(int ct = 1; ct <= 4; ct++){
                        change_tab(robot);
                        Thread.sleep(1000 * ct);
                        click(robot, 1060, 220);
                        Thread.sleep(2000);
                        click(robot, 1060, 400);
                        Thread.sleep(2000);
                    }

                    Thread.sleep(45000);
                    count = 0;

                    for(int ct = 1; ct <= 4; ct++){
                        close_tab(robot);
                        Thread.sleep(100);
                    }
                }
                
                count++;
            }
        }
        catch (Exception ex) 
        { 
            System.out.println("Oh no1!");
        }
        
    }
}