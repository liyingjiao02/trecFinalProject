import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

/**
 * Created by changxu on 17-6-16.
 */
class Title{
    public ArrayList<Integer> listId;
    public ArrayList<String> listTitle;
    Title(){
        this.listId = new ArrayList<>();
        this.listTitle = new ArrayList<>();
    }
}
public class Utils {
    private static Title getTitle(String path){
        Title title = new Title();

        try{
            FileReader fr = new FileReader(path);
            BufferedReader  bf = new BufferedReader(fr);
            String line = null;
            while((line = bf.readLine()) != null){

                if(line.contains("<num> Number:")){
                    String temp = line.replace("\n", "");
                    String [] temp1 = temp.split(" ");
                    title.listId.add(Integer.parseInt(temp1[2]));
                    continue;
                }
                if(line.contains("<title> ")){
                    String temp = line.replace("\n","");
                    String temp1 = temp.replace("<title> ", "");
                    title.listTitle.add(temp1);
                }
            }

            bf.close();
        }catch(Exception e) {
            e.printStackTrace();
        }
        return title;
    }

    
    private static Title getTitleExpansion(String path){
        Title title = new Title();
        try{
            FileReader fr = new FileReader(path);
            BufferedReader  bf = new BufferedReader(fr);
            String line = null;
            //344:Abuses of E-Mail  atrocities^0.192193660879 genocide^0.166896240572 genocidal^0.14710311955 
            while((line = bf.readLine()) != null){
                String [] temp1 = line.split(":");// temp1.length():2    
                title.listId.add(Integer.parseInt(temp1[0]));
                title.listTitle.add(temp1[1]);
            }
            bf.close();
        }catch(Exception e) {
            e.printStackTrace();
        }   
        return title;
    }
    
    
    
    
    
    
    
    
    public static void main(String[] args) {

        //try {
            /*FileWriter fw = new FileWriter("/home/changxu/study/trec/core_nist_id_title.txt");
            BufferedWriter bw = new BufferedWriter(fw);
            String path = "/home/changxu/study/trec/2017/core_nist.txt";
            Title title;
            title = Utils.getTitle(path);
            System.out.println(title.listId.get(2));
            System.out.println(title.listTitle.get(2));

            System.out.println(title.listId.size());
            System.out.println(title.listTitle.size());
            for (int i=0;i<title.listId.size();i++){
                bw.write(title.listId.get(i) + ":" + title.listTitle.get(i));
                bw.write("\n");*/
            String path = "/home/trec/automaticQueryExpansion/queryExpansionResultWith2.3Incremental.txt";
            Title title = Utils.getTitleExpansion(path);
            System.out.println(title.listId.size());
            System.out.println(title.listTitle.size());
            System.out.println(title.listId.get(0));
            System.out.println(title.listTitle.get(0));

        //} catch (IOException e) {
            
        //    e.printStackTrace();
        //}
    }
}
