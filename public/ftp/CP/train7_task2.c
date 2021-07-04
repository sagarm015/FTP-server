#include<stdio.h>
void main()
{
int dd,mm,yyyy ;
printf("enter the date you want to test \n");
scanf("%d/%d/%d",&dd, &mm, &yyyy);
printf("\n");
int valid=1 , leapyr;
char rsn;
if(yyyy<1900||yyyy>2100||dd>31||dd<1||mm<1||mm>12)
{ 
printf("the date dosen't exist");
valid=0;
}

else
{
 if(mm==4||mm==6||mm==9||mm==11)
  {
    if(dd==31)
    { printf("the dat enter is invalid as the month entered has only 30 days");
      valid=0;
    }
  }
 if(mm==2)
{
leapyr=(yyyy%4==0 &&yyyy%100!=0 )||yyyy%400==0;
if(leapyr==1)
{
  if(dd>29)
  { printf("this month in this year dont have days greater than 29");
    valid=0;
  }
}
else
 { if(dd>28)
   {
      printf("this month in this year dosent have days greater than 28");
      valid =0;
   } 
 }
}
}
if(valid==1)
{ printf("the date is absoultely valid :)");
}
}
