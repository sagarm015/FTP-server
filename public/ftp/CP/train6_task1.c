
#include<stdio.h>
#include<math.h>
void main()
{
 float ha,hb,v1,diff,u1,u2,u3,u4 ;
 float  t1_sq,t1,vel_g,t2,v,sum;
 printf("enter the height of A and B");
 scanf("%f %f",&ha,&hb);
 // let time taken for A ball to reach ground be t1
t1_sq=(2*ha)/10;
t1=sqrt(t1_sq);
// let velocity of balls after time t1 be v1 ( same for ball A and B)
v1=10*t1;
// diff in height between balls when A collides with ground
diff=hb-ha ;
// let velocity after hitting ground be vel_g if v is before hitting ground
v=v1;
vel_g= (sqrt(3)*v)/2;
// now first collision between balls will take place
//let time taken to collide after A hits ground be t2
t2=diff/(v1+vel_g);
//in ball to ball collison let thier intial velocities be u1 and u2
u1=vel_g-10*t2;
u2=v1 + 10*t2 ;
float k,x,y,u6,u5,t3,t4;
k=u1-u2;

// after ball to ball collision thier vel will be u3 and u4 
//u1-u2=u4-u3
// also , u3*u3 + u4*u4 = 0.67(u1*u1 + u2*u2)
// u4=u3-34.10
sum=0.67*(u1*u1 + u2*u2);
//u3*u3 + u4*u4 = 23719.38
//hence we have two eqauation and two variables
u3=(34+sqrt(34*34 +4*1*11281.69))/2;
u4=u3-34.10;
x=vel_g*t2 -0.5*10*t2*t2 ; // the height at which  collision took place
t3=(-(u3/5)+sqrt(u3*u3/25 +4*x/5))/2;
u5=u3 +10*t3;
u6=1.73*0.5*u5;
y=(u4*u4)/20;
s=x+y;
t4=s/u6;
z=u6*t4-0.5*10*t4*t4;
 







}
