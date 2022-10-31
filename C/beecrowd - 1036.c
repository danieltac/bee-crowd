#include <stdio.h>
#include <math.h>
int main (void){
  double a, b, c, x1, x2, delta, raizd;
  scanf ("%lf %lf %lf", &a,&b,&c);
  delta = (b*b) - 4*a*c;
  
  if ((delta > 0) && (a!=0)){
    raizd = sqrt(delta);
    x1 = ((-b) + raizd) / (2*a);
    x2 = ((-b) - raizd) / (2*a);
    printf("R1 = %.5lf\n", x1);
    printf("R2 = %.5lf\n", x2);

  }
  else{
    printf("Impossivel calcular\n");
  }
}