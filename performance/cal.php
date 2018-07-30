<?php

   function cal($n)
   {
      if($n <= 0) 
         return 0;
      else
         return $n+cal($n-1);
   }


   $n=10000;
   $value=cal($n);

   echo $value,"\n";
