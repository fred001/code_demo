#include <stdio.h>

int cal(int n)
{
  if( n <=0 ) return 0;

  return n+cal(n-1);
}

int main(int argc,char*argv[])
{
  int total=0;

  int n=10000;
  

  total=cal(n);


  printf("%d\n",total);
}

