package main

import "fmt"

var total int = 0
var n int = 10000

func cal(n int) int{
  if n <=0 {
    return 0
  } else{
    return n+cal(n-1)
  }
}


func main(){
  total=cal(n)
  fmt.Println(total)
}
