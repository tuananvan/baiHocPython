import turtle

t = turtle.Turtle()
t.speed(12) #Tốc độ vòng quay
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"] #màu
turtle.bgcolor("black")
for i in range(360):
    t.color(colors[i % 7])
    t.circle(100) #mỗi vòng tròn có bán kính 100
    t.right(5) #quay 5 độ sau mỗi vòng tròn
turtle.done()