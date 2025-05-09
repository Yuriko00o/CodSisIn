import turtle

class TurtleForMoobs:
    def test(self):
        skk=turtle.Turtle()
        for i in range(4):
            skk.forward(50)
            skk.right(90)
        turtle.done

    def estrella(self):
        est=turtle.Turtle()
        est.right(75)
        est.forward(100)
        for i in range(4):
            est.right(144)
            est.forward(100)
        turtle.done 

    def circulo(self):
        circ=turtle.Turtle
        circ.right(90)
        circ.forward(100)
        for i in range(50):
            circ.right(110)
            circ.forward(2)

t=TurtleForMoobs()
t.circulo()