import turtle as t



t.speed(100)



for i in range(8):
   for colors in ["red", "lime", "yellow", "white", "indigo", "magenta", "green", "brown"]:
       t.color(colors)
       for i in range(4):
            t.forward(200)
            t.left(91)

t.mainloop()