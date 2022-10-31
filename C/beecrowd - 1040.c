#include <stdio.h>

int main(void){
  double a, b, c, d, med, exam, novo;
  scanf("%lf %lf %lf %lf", &a,&b,&c,&d);
  med = ((a*2)+(b*3)+(c*4)+d)/10;
  if (med >= 7){
    printf("Media: %.1lf\n", med);
    printf("Aluno aprovado.\n");
  }
  else if (med >= 5.0 && med < 7.0){
    scanf("%lf", &exam);
    novo = (exam + med)/2;
    if (novo > 5){
      printf("Media: %.1lf\n",med);
      printf("Aluno em exame.\n");
      printf("Nota do exame: %.1lf\n", exam);
      printf("Aluno aprovado.\n");
      printf("Media final: %.1lf\n", novo);
    }
    else{
      printf("Media: %.1lf\n",med);
      printf("Aluno em exame.\n");
      printf("Nota do exame: %.1lf\n", exam);
      printf("Media final: %.1lf\n", novo);
      printf("Aluno reprovado.\n");
    }
  }
  else {
    printf("Media: %.1lf\n",med);
    printf("Aluno reprovado.\n");
  }
}