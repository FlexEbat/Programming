
#include <stdio.h>
// Печатает таблицу температур по фаренгейту и цельсию для fahr = 0, 20, .., 300 
/* int main () {
printf("Преобразование температуры из Фаренгейта в Цельсия\n");
    float fahr, celsius;
    int lower, upper, step;

    lower = 0; // Нижня граница 
    upper = 300; // Верхняя
    step = 20; // шаг
    fahr = lower;

    while (fahr <= upper) {
        celsius = (5.0/9.0) * (fahr-32.0);
        printf("%3.0f %6.1f\n", fahr, celsius);
        fahr = fahr + step;
    }
}
    */
#include <stdio.h>
/* печать таблицы температур по Фаренгейту и Цельсию */
int main()
{
    int fahr;
    for (fahr = 0; fahr <= 300; fahr = fahr + 20)
        printf ("%3d %6.1f\n", fahr, (5.0/9.0)*(fahr-32));
}
