import  turtle as t
import random as r


def cember(yaricap):
    t.speed(20)
    t.circle(yaricap)


renk = ["red", "yellow", "green", "blue", "indigo", "teal"]



for i in range(12):
    for i in range(6):
        t.color(renk[r.randint(0,5)])
        cember(i*20)

    t.left(90)

    for i in range(6):
        t.color(renk[r.randint(0, 5)])
        cember(i * 20)


t.left(120)

for i in range(12):
    for i in range(6):
        t.color(renk[r.randint(0,5)])
        cember(i*20)

    t.left(90)

    for i in range(6):
        t.color(renk[r.randint(0, 5)])
        cember(i * 20)





t.mainloop()