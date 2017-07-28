import java.net.HttpURLConnection;
import java.net.URL;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by changxu on 17-6-16.
 */
public class getFromUrl {
    public List<String> doc_id;
    public List<String> score;
    public  getFromUrl(){
        doc_id = new ArrayList<>();
        score = new ArrayList<>();
    }
    public String getURLContent(String urlStr) {
        /** 网络的url地址 */
        URL url = null;
        /** http连接 */
        HttpURLConnection httpConn = null;
         /**//** 输入流 */
        BufferedReader in = null;
        StringBuffer sb = new StringBuffer();
        try{
            url = new URL(urlStr);
            in = new BufferedReader(new InputStreamReader(url.openStream(),"UTF-8"));
            String str = null;
            String[] tmp;
            while((str = in.readLine()) != null) {
                if (str.contains("\"id\":")){
                    tmp = str.split("\"");
                    doc_id.add(tmp[3]);
                }
                if (str.contains("\"score\":")){
                    tmp = str.split(":");
                    score.add(tmp[1].split("}")[0]);
                }
                sb.append(str + "\n");
            }
        } catch (Exception ex) {

        } finally{
            try{
                if(in!=null) {
                    in.close();
                }
            }catch(IOException ex) {
            }
        }
        String result =sb.toString();
//        System.out.println(result);
        return result;
    }

    public static void main(String args[]){
//        String url = "http://localhost:8983/solr/trec/select?fl=id%20score&indent=on&wt=json&q=New%20Hydroelectric%20Projects";
       
        //http://10.61.1.136:8983/solr/trec1/select?indent=on&q=*:*%20New%20Hydroelectric%20Projects&rows=11&wt=json
        //http://10.61.1.136:8983/solr/trec1/select?indent=on&q=*:*%20New^2%20%20Hydroelectric^2%20%20Projects&rows=11&wt=json
        String url = "http://10.61.1.136:8983/solr/trec1/select?fl=id%20score&indent=on&rows=5&start=0&wt=json&q=New%20Hydroelectric%20Projects";
        getFromUrl test = new getFromUrl();
        test.getURLContent(url);
        System.out.println(test.doc_id.size());
        System.out.println(test.score.size());

        for (int i = 0; i<test.doc_id.size();i++){
            System.out.println(test.doc_id.get(i) + " " + test.score.get(i));
        }
    }
}
