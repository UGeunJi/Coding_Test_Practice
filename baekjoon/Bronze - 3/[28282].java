import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st=new StringTokenizer(br.readLine());
        int x=Integer.parseInt(st.nextToken());
        int k=Integer.parseInt(st.nextToken());
        st=new StringTokenizer(br.readLine());
        int[] color=new int[k+1];
        for(int i=0; i<x; i++){
            color[Integer.parseInt(st.nextToken())]++;
        }
        long answer=0;
        for(int i=0; i<x; i++){
            answer+=x-color[Integer.parseInt(st.nextToken())];
        }
        bw.write(answer+"");
        bw.flush();

    }
}
