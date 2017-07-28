import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

/**
 * Created by changxu on 17-6-16.
 */

class PerLineFormat{
    int titleId;
    String queryNumber = "Q0";
    int docId;
    int rank;
    double score;
    String runTag;
    public PerLineFormat(int titleId, int docId, int rank, double score, String runTag){
        this.titleId = titleId;
        this.docId = docId;
        this.rank = rank;
        this.score = score;
        this.runTag = runTag;
    }
}

public class WriteSubmission {
    public static void writeToFile(ArrayList<PerLineFormat> result, String path){
        try {
            FileWriter fw = new FileWriter(path);
            BufferedWriter bw = new BufferedWriter(fw);
            for(PerLineFormat line : result){
                bw.write(String.valueOf(line.titleId));
                bw.write(" ");
                bw.write(line.queryNumber);
                bw.write(" ");
                bw.write(String.valueOf(line.docId));
                bw.write(" ");
                bw.write(String.valueOf(line.rank));
                bw.write(" ");
                bw.write(String.valueOf(line.score));
                bw.write(" ");
                bw.write(line.runTag);
                bw.write("\n");
            }
            bw.close();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
    public static void main(String[] args) {
        ArrayList<PerLineFormat> list = new ArrayList<>();
        PerLineFormat line1 = new PerLineFormat(200, 000001, 1, 23.0003432, "ICT001");
        PerLineFormat line2 = new PerLineFormat(200, 000002, 2, 22.0003432, "ICT001");
        list.add(line1);
        list.add(line2);
        String path = "testResult.txt";
        WriteSubmission.writeToFile(list, path);
    }
}

