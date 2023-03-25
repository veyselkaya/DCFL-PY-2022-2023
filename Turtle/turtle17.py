import turtle as t

t.speed(20)

renk = ["red", "yellow", "green", "blue", "indigo", "teal"]

# for i in range(36):
#     t.color(renk[i%6])
#     t.circle(i*5)
#     t.circle(-i*5)
#     t.left(i)



def kare(kenar):
    t.speed(100)
    for i in range(4):
        t.forward(kenar)
        t.left(90)

for i in range(10):
    t.color(renk[i%6])
    kare(i*10)
    kare(-i*10)
    t.left(i)

t.mainloop()