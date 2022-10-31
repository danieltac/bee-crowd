#include <stdio.h>
char nome;
double salf;
double ttv;
int main() {
    scanf("%s", &nome);
    scanf("%lf", &salf);
    scanf("%lf", &ttv);
    salf = salf + (ttv*0.15);
    printf("TOTAL = R$ %.2lf\n", salf);
    return 0;
}