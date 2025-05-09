import turtle
class TurtleForMoobs:
    def copoDeNieve(self):
        turtle.reset()
        turtle.ht()
        for i in range(3):
            self.ks(200,3)
            turtle.left(120)
            turtle.update()
            turtle.done
    def ks(self,length,d):
        if d==0:
            turtle.forward(length)
        else:
            length=length/3
            d=d-1
            self.ks(length,d)
            turtle.right(66)
            self.ks(length,d)

