#include <stdio.h>
#include <math.h>

int main ()
{
   int a[4]= {10,20,30,40};
   int *p;
   p =&a[0];
   printf("%d\n",*++p);
   printf("%d\n",++*p);
   printf("%d\n",++p);
   printf("%d",*++p);
   return 0;
}
