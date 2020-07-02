import turtle
from tkinter import *
def square(width):
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)

def reset():
    turtle.penup()
    turtle.goto(original)
    turtle.pendown()

def matrix(len):#画表格 大小可调
    for x in range(0,len):
        for y in range(0,len):
            square(width)
            turtle.penup()
            turtle.forward(width)
            turtle.pendown()
        turtle.penup()
        turtle.backward(len*width)
        turtle.right(90)
        turtle.forward(width)
        turtle.left(90)
        turtle.pendown()
        
def letters(len):
    if len==13:
        turtle.penup()
        turtle.goto(ox+10,oy)
        turtle.write("A",font = ("Arial",18,"bold"))
        turtle.penup()
        turtle.forward(width)
        turtle.pendown()
        turtle.write("K",font = ("Arial",18,"bold"))
        turtle.penup()
        turtle.forward(width)
        turtle.pendown()
        turtle.write("Q",font = ("Arial",18,"bold"))
        turtle.penup()
        turtle.forward(width)
        turtle.pendown()
        turtle.write("J",font = ("Arial",18,"bold"))
        turtle.penup()
        turtle.forward(width)
        turtle.pendown()
        turtle.write("T",font = ("Arial",18,"bold"))
        turtle.penup()
        turtle.forward(width)
        turtle.pendown()
        turtle.write("9",font = ("Arial",18,"bold"))
        turtle.penup()
        turtle.forward(width)
        turtle.pendown()
        turtle.write("8",font = ("Arial",18,"bold"))
        turtle.penup()
        turtle.forward(width)
        turtle.pendown()
        turtle.write("7",font = ("Arial",18,"bold"))
        turtle.penup()
        turtle.forward(width)
        turtle.pendown()
        turtle.write("6",font = ("Arial",18,"bold"))
        turtle.penup()
        turtle.forward(width)
        turtle.pendown()
        turtle.write("5",font = ("Arial",18,"bold"))
        turtle.penup()
        turtle.forward(width)
        turtle.pendown()
        turtle.write("4",font = ("Arial",18,"bold"))
        turtle.penup()
        turtle.forward(width)
        turtle.pendown()
        turtle.write("3",font = ("Arial",18,"bold"))
        turtle.penup()
        turtle.forward(width)
        turtle.pendown()
        turtle.write("2",font = ("Arial",18,"bold"))
        reset()
        turtle.penup()
        turtle.goto(ox-23,oy-30)#-23 -30
        turtle.write("A",font = ("Arial",18,"bold"))
        turtle.right(90)
        turtle.forward(width)
        turtle.left(90)
        turtle.write("K",font = ("Arial",18,"bold"))
        turtle.right(90)
        turtle.forward(width)
        turtle.left(90)
        turtle.write("Q",font = ("Arial",18,"bold"))
        turtle.right(90)
        turtle.forward(width)
        turtle.left(90)
        turtle.write("J",font = ("Arial",18,"bold"))
        turtle.right(90)
        turtle.forward(width)
        turtle.left(90)
        turtle.write("T",font = ("Arial",18,"bold"))
        turtle.right(90)
        turtle.forward(width)
        turtle.left(90)
        turtle.write("9",font = ("Arial",18,"bold"))
        turtle.right(90)
        turtle.forward(width)
        turtle.left(90)
        turtle.write("8",font = ("Arial",18,"bold"))
        turtle.right(90)
        turtle.forward(width)
        turtle.left(90)
        turtle.write("7",font = ("Arial",18,"bold"))
        turtle.right(90)
        turtle.forward(width)
        turtle.left(90)
        turtle.write("6",font = ("Arial",18,"bold"))
        turtle.right(90)
        turtle.forward(width)
        turtle.left(90)
        turtle.write("5",font = ("Arial",18,"bold"))
        turtle.right(90)
        turtle.forward(width)
        turtle.left(90)
        turtle.write("4",font = ("Arial",18,"bold"))
        turtle.right(90)
        turtle.forward(width)
        turtle.left(90)
        turtle.write("3",font = ("Arial",18,"bold"))
        turtle.right(90)
        turtle.forward(width)
        turtle.left(90)
        turtle.write("2",font = ("Arial",18,"bold"))
        turtle.pendown()
        reset()
    else:
        pass
    

def draw(width,locationx,locationy,color):
    locationx = (13 - locationx)*width
    locationy = (13 - locationy)*width
    
    turtle.penup()
    turtle.goto(ox+locationx+2,oy-locationy-2)
    turtle.begin_fill()
    turtle.color(color)
    square(width-3)
    turtle.end_fill()
    
def drawsinglecombo(defaultinput,color):
    for x in defaultinput.split(","):
        if len(x)==2:
            draw(width,dic[x[0]],dic[x[1]],color)
        elif len(x)==3 and (x[2]=='o' or x[2]=='O'):
            draw(width,dic[x[0]],dic[x[1]],color)
        elif len(x)==3 and (x[2]=='s' or x[2]=='S'):
            draw(width,dic[x[1]],dic[x[0]],color)
        
def cleanall():
    for x in range(1,14):
        for y in range(1,14):
            draw(width,x,y,"whitesmoke")

# def dragging(x, y):
#     turtle.ondrag(None)
#     drawwhenuclick1(x, y)
#     t.ondrag(dragging)

def drawwhenuclick1(x,y):# (-200,200 is the original point)
    turtle.ondrag(None)
    print(x,y)
    
    locationx=0
    locationy=0
    if x>-200 and x<-170:
        locationx = 13
    elif x>-170 and x<-140:
        locationx = 12
    elif x>-140 and x<-110:
        locationx = 11
    elif x>-110 and x<-80:
        locationx = 10
    elif x>-80 and x<-50:
        locationx = 9
    elif x>-50 and x<-20:
        locationx = 8
    elif x>-20 and x<10:
        locationx = 7
    elif x>10 and x<40:
        locationx = 6
    elif x>40 and x<70:
        locationx = 5
    elif x>70 and x<100:
        locationx = 4
    elif x>100 and x<130:
        locationx = 3
    elif x>130 and x<160:
        locationx = 2
    elif x>160 and x<190:
        locationx = 1
    if y>170 and y<200:
        locationy = 13
    elif y>140 and y<170:
        locationy = 12
    elif y>110 and y<140:
        locationy = 11
    elif y>80 and y<110:
        locationy = 10
    elif y>50 and y<80:
        locationy = 9
    elif y>20 and y<50:
        locationy = 8
    elif y>-10 and y<20:
        locationy = 7
    elif y>-40 and y<-10:
        locationy = 6
    elif y>-70 and y<-40:
        locationy = 5
    elif y>-110 and y<-70:
        locationy = 4
    elif y>-140 and y<-110:
        locationy = 3
    elif y>-170 and y<-140:
        locationy = 2
    elif y>-200 and y<-170:
        locationy = 1
    if locationx!=0 and locationy!=0:
        draw(width,locationx,locationy,"orange")
    turtle.ondrag(drawwhenuclick1)


def drawwhenuclick2(x,y):# (-200,200 is the original point)
    locationx=0
    locationy=0
    if x>-200 and x<-170:
        locationx = 13
    elif x>-170 and x<-140:
        locationx = 12
    elif x>-140 and x<-110:
        locationx = 11
    elif x>-110 and x<-80:
        locationx = 10
    elif x>-80 and x<-50:
        locationx = 9
    elif x>-50 and x<-20:
        locationx = 8
    elif x>-20 and x<10:
        locationx = 7
    elif x>10 and x<40:
        locationx = 6
    elif x>40 and x<70:
        locationx = 5
    elif x>70 and x<100:
        locationx = 4
    elif x>100 and x<130:
        locationx = 3
    elif x>130 and x<160:
        locationx = 2
    elif x>160 and x<190:
        locationx = 1
    else:
        pass
    if y>170 and y<200:
        locationy = 13
    elif y>140 and y<170:
        locationy = 12
    elif y>110 and y<140:
        locationy = 11
    elif y>80 and y<110:
        locationy = 10
    elif y>50 and y<80:
        locationy = 9
    elif y>20 and y<50:
        locationy = 8
    elif y>-10 and y<20:
        locationy = 7
    elif y>-40 and y<-10:
        locationy = 6
    elif y>-70 and y<-40:
        locationy = 5
    elif y>-110 and y<-70:
        locationy = 4
    elif y>-140 and y<-110:
        locationy = 3
    elif y>-170 and y<-140:
        locationy = 2
    elif y>-200 and y<-170:
        locationy = 1

    if locationx!=0 and locationy!=0:
        draw(width,locationx,locationy,"red")
    
def drawwhenuclick3(x,y):# (-200,200 is the original point)
    locationx=0
    locationy=0
    if x>-200 and x<-170:
        locationx = 13
    elif x>-170 and x<-140:
        locationx = 12
    elif x>-140 and x<-110:
        locationx = 11
    elif x>-110 and x<-80:
        locationx = 10
    elif x>-80 and x<-50:
        locationx = 9
    elif x>-50 and x<-20:
        locationx = 8
    elif x>-20 and x<10:
        locationx = 7
    elif x>10 and x<40:
        locationx = 6
    elif x>40 and x<70:
        locationx = 5
    elif x>70 and x<100:
        locationx = 4
    elif x>100 and x<130:
        locationx = 3
    elif x>130 and x<160:
        locationx = 2
    elif x>160 and x<190:
        locationx = 1
    else:
        pass
    if y>170 and y<200:
        locationy = 13
    elif y>140 and y<170:
        locationy = 12
    elif y>110 and y<140:
        locationy = 11
    elif y>80 and y<110:
        locationy = 10
    elif y>50 and y<80:
        locationy = 9
    elif y>20 and y<50:
        locationy = 8
    elif y>-10 and y<20:
        locationy = 7
    elif y>-40 and y<-10:
        locationy = 6
    elif y>-70 and y<-40:
        locationy = 5
    elif y>-110 and y<-70:
        locationy = 4
    elif y>-140 and y<-110:
        locationy = 3
    elif y>-170 and y<-140:
        locationy = 2
    elif y>-200 and y<-170:
        locationy = 1

    if locationx!=0 and locationy!=0:
        draw(width,locationx,locationy,"whitesmoke")


if __name__ == "__main__":
    # turtle.tracer(0)
    # turtle.delay(0)
    # turtle.ht()
    # turtle.screensize(canvwidth=None, canvheight=None, bg='whitesmoke')
    # turtle.setup(500,500)
    # turtle.pensize(3)
    # turtle.speed(0)
    # # turtle.onscreenclick(drawwhenuclick1,btn=1,add=None)
    # # turtle.ondrag(dragging)
    # turtle.onscreenclick(drawwhenuclick1,btn=1,add=None)
    # turtle.onscreenclick(drawwhenuclick2,btn=2,add=None)
    # turtle.onscreenclick(drawwhenuclick3,btn=3,add=None)

    #---- turtle setup ----
    # width = 30 #表格宽度
    # ox = -200
    # oy = 200
    # original = (ox,oy)#起始点
    # reset()
    # turtle.ht()
    # #---- input setup ----
    # cards = "A K Q J T 9 8 7 6 5 4 3 2"
    # dic = {"A":13,"K":12,"Q":11,"J":10,"T":9,"9":8,"8":7,"7":6,"6":5,"5":4,"4":3,"3":2,"2":1}
    # cardlist = cards.split()
    # #---- main setup ----
    # end = False
    # letters(13)
    # matrix(13)

    # '''

    # while end ==False:

    #     color ="palegreen"
    #     askforrange = input("欢迎使用QuanPoker起手表生成器！\n请按以下格式输入翻前范围：\n对子：AA 同花AKS或AKs 非同花AKO或AKo\n所有组合用逗号隔开\n默认黄色，输入1切换至绿色，输入3切换至蓝色\n输入X清屏\n")
    #     askforrange.split(",")
    #     if askforrange[-1] =="1":
    #         color ="palegreen"
    #     elif askforrange[-1] =="2":
    #         color ="red"
    #     elif askforrange[-1] =="3":
    #         color ="orange"
    #     elif askforrange[-1] =="X":
    #         cleanall()
    #     elif askforrange[-1] =="x":
    #         break
    #     drawsinglecombo(askforrange,color)'''
    # turtle.mainloop()

    # initialize tk
    root = Tk()

    # def key(evnt):
    #     print("preessed", repr(event.char))

    # drawing function
    def callback(event):
        frame.focus_set()
        print("clicked at", event.x, event.y)

    # define frame to plot
    frame = Frame(root, width=100, height=100)
    # frame.bind("<Key>", key)

    # bind with btn 1 held down and motion
    frame.bind("<B1-Motion>", callback)
    frame.pack()

    root.mainloop()
