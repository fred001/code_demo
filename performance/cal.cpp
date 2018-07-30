#include <iostream>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <fcntl.h>
#include <unistd.h>

#include <time.h>

#include <sys/stat.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <dirent.h>
#include <signal.h>

/*
 * copy file
 *
 * file:copyfile.cpp
 * compile: g++ copyfile.cpp
 */

using namespace std;

int cal(int n)
{
  if (n <=0 ) return 0;

  return n+cal(n-1);
}


int
main()
{
  int total=0;
  int n=10000;

  total=cal(n);

  cout << total << "\n"<< endl;

  return 0;
}
