import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

/**
 * Created by changxu on 17-6-16.
 */
public class mainClass {
    String queryNumber = "Q0";
    String runTag = "ICT17ZCJL06";
    public void readTopic(String inpath, String outpath) throws IOException {
        FileReader fr = new FileReader(inpath);
        BufferedReader br = new BufferedReader(fr);
        FileWriter fw = new FileWriter(outpath);
        BufferedWriter bw = new BufferedWriter(fw);
        String str;
        String tmp[];
        String topic_id;
        String topic;
        
        String queryProfix = "http://10.61.1.136:8983/solr/trec1/select?fl=id%20score&indent=on&rows=10000&start=0&wt=json&q=";
        String query;
        int count = 0;
        while((str = br.readLine()) != null){
            count += 1;
            tmp = str.split(":");
            topic_id = tmp[0];
            topic = tmp[1];
            query = queryProfix + topic.trim().replace(" ", "%20");
            getFromUrl gfu = new getFromUrl();
            gfu.getURLContent(query);
            System.out.print(gfu.doc_id.size());   //debug
            System.out.print(":");//debug
            System.out.print(gfu.score.size());//debug
            System.out.print("\n");//debug
            if(gfu.doc_id.size() == 0){
                System.out.print(topic_id);//debug
                System.out.print(":");//debug
                System.out.print(topic);//debug
                System.out.print("\n");
                System.out.print("query");//debug
                System.out.print(":");//debug
                System.out.print(query);
                System.out.print("\n");
            }
            writeSubmission(bw,topic_id,queryNumber,gfu.doc_id, gfu.score, runTag);
//            for (int i = 0; i<gfu.doc_id.size();i++){
//                System.out.println(gfu.doc_id.get(i) + " " + gfu.score.get(i));
//            }
//            System.out.println(query);
        }
        System.out.println("process is over");
    }

    private void writeSubmission(BufferedWriter bw, String topicId, String queryNumber, List<String> docId, List<String> score, String runTag) throws IOException {
        for (int i=0;i < docId.size();i++){
            
            int id = Integer.parseInt(docId.get(i));
            String docIdFormat = String.format("%07d", id);              
            
            bw.write(topicId + " ");
            bw.write(queryNumber + " ");
            bw.write(docIdFormat + " ");
            bw.write(String.valueOf(i) + " ");
            bw.write(score.get(i) + " ");
            bw.write(runTag + "\n");
        }
        bw.flush();
    }

    public static void main(String args[]) throws IOException {
        mainClass mainprocess = new mainClass();
        //String inputpath = "/home/changxu/study/trec/queryExpansion.txt";
        //String inputpath = "/home/trec/automaticQueryExpansion/queryExpansionResult2_1nostop.txt";       
        
        String inputpath = "/home/trec/automaticQueryExpansion/queryExpansionResult2_3nostopRankTitle1_5.txt";       
        String outputpath = "/home/trec/jiaoliying/solr_java/src/core_nist_submission_expansion_2_3nostopRankTitle1_5.txt";
        mainprocess.readTopic(inputpath, outputpath);
    }
}
