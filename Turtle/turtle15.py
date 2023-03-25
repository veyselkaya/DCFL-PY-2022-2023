import  turtle as t

def kare(kenar, x, y):
    t.speed(100)
    for i in range(4):
        t.forward(kenar)
        t.left(90)
    t.penup()
    t.goto(x,y)
    t.pendown()


for i in range(36):
    kare(50, 20,20)
    t.left(10)






t.mainloop()