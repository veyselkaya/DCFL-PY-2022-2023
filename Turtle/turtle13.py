import turtle as t


t.speed(100)


for i in range(10):

    for i in range(3):
        t.forward(100)
        t.left(120)
        t.circle(10)

    t.penup()
    t.forward(200)
    t.pendown()

    for i in range(3):
        t.forward(100)
        t.left(120)
        t.circle(10)

    t.penup()
    t.left(180)
    t.forward(300)

    t.pendown()

    for i in range(3):
        t.forward(100)
        t.left(120)
        t.circle(10)

    t.left(5)



t.mainloop()


#ödev: bir dikdörtgenin ortasına bir kare, karenin ortasına bir üçgen, üçgenin ortasına daire çizniz
#ödev: MERHABA yazısını yazdırın
#bir ev, arkasında dağlar, havada 2 bulut, bahçede 2 ağaç çizniz...