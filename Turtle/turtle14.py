import  turtle as t


def kare(kenar):
    t.speed(100)
    for i in range(4):
        t.forward(kenar)
        t.left(90)

def cember(yaricap):
    t.circle(yaricap)


def ucgen(kenar2):
    for i in range(3):
        t.forward(kenar2)
        t.left(120)



t.mainloop()