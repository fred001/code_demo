/**
 * java开发过程：
 *  1， 创建文件  Hello.java
 *  2,  编写代码，如本内容
 *  3， 编译  javac  Hello.java (yum -y install java-devel)
 *  4,  编译成功则生成  Hello.class 二进制文件
 *  5， 运行  java Hello   (不用加class,加了反而是错的)
 */
public class Calculate //类名和文件名一致
{
  public static void main(String[] args) //入口方法
  {
    int total=0;
    int n=10000;

    Calculate caltater=new Calculate();

    total=caltater.cal(n);

    System.out.println(total);
  }

  int cal(int n)
  {
    if(n <=0 ) return 0;

    return n+cal(n-1);
  }

}
