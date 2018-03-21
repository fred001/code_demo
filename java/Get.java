/*
 *Usage:
 * 依赖Okhttp3, okhttp3依赖okio
 * 它们都位于 ./lib/ 下
 *
 * 编译：javac -Djava.ext.dirs=lib Get.java
 * 运行：java -Djava.ext.dirs=lib Get
 */
import java.util.*;
import java.io.IOException;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.FormBody;;
import okhttp3.Response;
import com.google.gson.Gson;

public class Get 
{
  public static void main(String[] args) 
  {
    String url="http://example.com/api/";

    FormBody.Builder formBody =new FormBody.Builder();
    formBody.add("mobile","MOBILE");
    formBody.add("password","PASSWORD");

    RequestBody body=formBody.build();


    OkHttpClient client = new OkHttpClient();
    try
    {
      url+="user/login/password";

      Request request = new Request.Builder().url(url)
        .post(body)
        .build();

      Response response = client.newCall(request).execute();


      Gson gson=new Gson();

      String str=response.body().string();
      
      WdResponse r=gson.fromJson(str,WdResponse.class);

      if(r.error)
      {
        System.out.println(r.data.get("user_id"));
      }
      else
      {
        //System.out.println(response.body().string());
      }
    }
    catch(Exception e)
    {
      System.out.println(e);
    }
  }
}


class WdResponse
{
  int error;
  Map data;
}
