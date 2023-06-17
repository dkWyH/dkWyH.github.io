import random
import time
import turtle
from string import whitespace
import math
placelist = {}    
i = 1
t = 0
life=0
turtle.hideturtle()    
turtle.screensize(800,800, "black")
turtle.pencolor(1,1,1)
turtle.fillcolor(1,1,1)
turtle.speed(9999999999999999999999999999999999999999999999999999999)
turtle.fillcolor(1,1,1)
def star():

 
    turtle.colormode(255) #切换颜色模式，turtle.colormode(cmode=None)返回颜色模式或将其设为 1.0 或 255。有1.0模式和255模式
    t1=turtle.Turtle()
    t2=turtle.Turtle() #创建两个对象，turtle1用来画圆，turtle2用来画五角星
 
    #画圆
    r=100 #半径为100
    t1.color((217,217,25),(217,217,25)) #前面一个参数是pencolor,后一个参数是fillcolor
    t1.pensize(3)
 
    t1.penup()
    t1.goto(0,200)
    t1.pendown()
    t1.begin_fill()
    t1.circle(r*(-1)-10) #其实原本半径为100,但是为了美观，就将半径放大了
    t1.end_fill()
    t1.hideturtle()
    #画五角星
    t2.color("red","red")
 
    t2.penup()
    t2.goto(r*(-1)*math.cos(math.pi/10),r*math.sin(math.sin(math.pi/10))+r)
    t2.pendown()
    t2.begin_fill()
    for i in range(0,5):
        t2.forward(100*math.cos(math.pi/10)*2)
        t2.right(144)
    t2.end_fill()
    t2.hideturtle()




turtle.tracer(3)    


while True:  
    for j in range(0,random.randint(0,50)):
        ran1=random.randint(1,10)
        if ran1!=1:
            placelist[i] = [random.uniform(1,1600),random.uniform(1,1600),0,random.uniform(10,100),'n','n']
            turtle.penup()
            turtle.setx(placelist[i][0]/2-400)
            turtle.sety(placelist[i][1]/2-400)
            turtle.pendown()
            turtle.dot(abs(placelist[i][3]/20),1,1,1)
        if ran1==1:
            placelist[i] = [random.uniform(1,1600),random.uniform(1,1600),1,random.uniform(10,100),random.uniform(0,1),random.uniform(0,1)]
            turtle.penup()
            turtle.setx(placelist[i][0]/2-400)
            turtle.sety(placelist[i][1]/2-400)
            turtle.pendown()
            turtle.dot(abs(placelist[i][3]/20),'gold')
            life = life+1
        i = i+1
    for j in range(0,random.randint(1,15)):
        ran2 = random.randint(1,len(placelist))
        if placelist[ran2][2]<1000 and placelist.get('math', 100) !=100:
            del placelist[ran2]
            turtle.penup()
            turtle.setx(placelist[ran2][0]/2-400)
            turtle.sety(placelist[ran2][1]/2-400)
            turtle.pendown()
            turtle.dot(abs(placelist[ran2][3]/50),0,0,0)
        else:
            placelist[ran2][3]= placelist[ran2][3]-200
            continue
    
    

    t = t+1
    print('宇宙已诞生'+str(4000000000+100*t)+'年.恒星数:'+str(len(placelist))+'文明数'+str(life))
    for k in placelist.items():
        print('宇宙已诞生'+str(4000000000+100*t)+'年.恒星数:'+str(len(placelist))+'文明数'+str(life)+str(k))
