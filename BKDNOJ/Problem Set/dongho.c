
#include <stdio.h>

int main()
{
    int gio, phut, giay;
    scanf("%d %d %d", &gio, &phut, &giay);
    if (gio == 23 && phut == 59 && giay == 59)
    {
        gio = 0;
        phut = 0;
        giay = 0;
    }
    else if (phut == 59 && giay == 59)
    {
        phut = 0;
        giay = 0;
        gio += 1;
    }
    else if (giay == 59)
    {
        phut += 1;
        giay = 0;
    }
    else
    {
        giay += 1;
    }
    printf("%d:%d:%d", gio, phut, giay);
}