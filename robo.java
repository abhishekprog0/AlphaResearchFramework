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
        delay(10);
        keyRelease(keyCode);
    }
}



public class robo
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

    public static void copy_text(String text)
    {
        //System.out.println(text);
        Clipboard clipboard = getSystemClipboard();
        clipboard.setContents(new StringSelection(text), null);
    }

    public static String get_from_clipboard() throws Exception {
        Clipboard clipboard = getSystemClipboard();

        String result = (String) clipboard.getData(DataFlavor.stringFlavor);
        System.out.println(result);
        return result;
       
    }

    private static Clipboard getSystemClipboard()
    {
        Toolkit defaultToolkit = Toolkit.getDefaultToolkit();
        Clipboard systemClipboard = defaultToolkit.getSystemClipboard();

        return systemClipboard;
    }

    public static void copy(Robot robot)
    {
        try{
            executeCommand(robot, KeyEvent.VK_C);
        }
        catch(Exception ex)
        {

        }
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
    /*
    public static void change_tab(Robot robot) throws AWTException
    {
        robot.keyPress(KeyEvent.VK_CONTROL);
        robot.keyPress(KeyEvent.VK_TAB);
        robot.keyRelease(KeyEvent.VK_CONTROL);
        robot.keyRelease(KeyEvent.VK_TAB);
    }*/

    public static void newTab(Robot robot) throws AWTException
    {
        System.out.println("Executing new tab command");
        robot.keyPress(KeyEvent.VK_META);
        robot.keyPress(KeyEvent.VK_T);
        robot.keyRelease(KeyEvent.VK_META);
        robot.keyRelease(KeyEvent.VK_T);
    }

    public static void click(Robot robot, int x, int y) throws AWTException
    {
        int mask = InputEvent.BUTTON1_DOWN_MASK;
        robot.mouseMove(x, y);           
        robot.mousePress(mask);     
        robot.mouseRelease(mask);
    }
    /*
    public static void cmd_tab(Robot robot) throws AWTException, IOException
    {
            robot.keyPress(KeyEvent.VK_META);
            robot.keyPress(KeyEvent.VK_TAB);
            robot.keyRelease(KeyEvent.VK_META);
            robot.keyRelease(KeyEvent.VK_TAB);
    }
    */
    public static void main(String[] args) throws IOException
    {
        try
        {
            //String content = new Scanner(new File("Alpha.txt")).useDelimiter("\\Z").next();
            //String[] data = content.split("@@");
            String url_default = "https://websim.worldquantchallenge.com/myalphas/os?page=";
            String url = new String();
            SuperRobot robot = new SuperRobot();
            PrintWriter writer = new PrintWriter("alphas.txt", "UTF-8");
            String alpha_list = new String();
            alpha_list = "";
            Thread.sleep(4000);

            for(int k = 0; k < 4; k++)
            {
                //System.out.println(k);

                Thread.sleep(10000);
                url = url_default + Integer.toString(k + 1);
                //copy url
                copy_text(url);
                Thread.sleep(500);

                click(robot, 900, 50);
                Thread.sleep(1000);

                select_all(robot);
                Thread.sleep(350);

                //paste url
                paste(robot);
                Thread.sleep(300);
                //press enter
                robot.typeKey(KeyEvent.VK_ENTER);

                //wait 5 secs
                Thread.sleep(15000);


                int x = 299;
                for(int i = 276; i <= 832; i += 29 )
                {
                    String alphas = new String();
                    
                    click(robot, x, i);
                    Thread.sleep(1000);

                    //click on textbox
                    click(robot, x, 413);
                    Thread.sleep(1500);

                    //select all
                    select_all(robot);
                    Thread.sleep(500);

                    //copy to clipboard
                    copy(robot);
                    Thread.sleep(500);

                    //get from clipboard
                    alphas = get_from_clipboard().replaceAll("\\s+","");

                    //append to text file
                    alpha_list += alphas + "@@";

                    click(robot, 75, 230);
                    Thread.sleep(500);

                }
                
            }       
            writer.println(alpha_list);
            writer.close();
        }
    
        catch (Exception ex) 
        { 
            System.out.println("Crap!");
        }
    }
}
