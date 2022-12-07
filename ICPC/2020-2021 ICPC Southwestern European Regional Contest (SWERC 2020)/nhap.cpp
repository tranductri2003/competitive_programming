#include <string.h>
#include <stdlib.h>
#include <dos.h>
#include "button.ta"
#include <iostream.h>
#include "mouse.inc"
/*----------------------Dinh_Nghia_Doi_Tuong-------------------------------*/
class Mouse
{
private:
    Button BUTTON1, BUTTON2;

public:
    void Show();
    void EnterClick();
    int Click();
    void Program();
    void Menu();
};
/*-------------------Hien_Thi_Cac_Nut_Bam----------------------------------*/
void Mouse::Show()
{
    int x = 20, y = 10;
    gotoxy(25, 5);
    textcolor(10);
    cprintf("YOU HAS TWO BUTTON");
    VarButton(BUTTON1, "[   BUTTON1   ]", x, y);
    VarButton(BUTTON2, "[   BUTTON2   ]", x + 20, y);
    ShowButton(BUTTON1);
    ShowButton(BUTTON2);
}
/*---------------------Nhan_Click_Chuot------------------------------------*/
void Mouse::EnterClick()
{
    do
    {
        MOUSE_THERE = 1;
        if (kbhit())
            getch();
        get_mouse_button(&lbutton, &rbutton, &xmouse, &ymouse);
    } while (lbutton == 0);
}
/*-----------------------Phan_Loai_Click-----------------------------------*/
int Mouse::Click()
{
    MOUSE_THERE = 0;
    if (ClickButton(BUTTON1, xmouse, ymouse))
    {
        EffectClick(BUTTON1); /*sau khi click chuot thi doi mau khac*/
        return 1;
    }
    if (ClickButton(BUTTON2, xmouse, ymouse))
    {
        EffectClick(BUTTON2); /*sau khi click chuot thi doi mau khac*/
        return 2;
    }
    return 3;
}
/*------------------------Cac_Chuc_Nang_Cua_Chuong_Trinh-------------------*/
void Mouse::Program()
{
    switch (Click())
    {
    case 1:
        clrscr();
        gotoxy(20, 10);
        textcolor(10);
        cprintf("YOU HAVE CLICK ON BUTTON 1. ENTER TO CONTINUE");
        getch();
        gotoxy(20, 10);
        clreol();
        break;
    case 2:
        clrscr();
        gotoxy(20, 10);
        textcolor(10);
        cprintf("YOU HAVE CLICK ON BUTTON 2. ENTER TO EXIT");
        getch();
        gotoxy(20, 10);
        clreol();
        exit(1);
        break;
    }
}
/*--------------------------Menu_Chinh-------------------------------------*/
void Mouse::Menu()
{
    while (1)
    {
        Show();
        EnterClick();
        Program();
    }
}
/*---------------------------Chuong_Trinh_Chinh----------------------------*/
int main()
{
    Mouse ob;
    ob.Menu();
    return 0;
}