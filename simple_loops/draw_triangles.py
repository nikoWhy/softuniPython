import turtle

my_turtle = turtle.Turtle()

my_turtle.shape('turtle')
n = 10

for i in range(0, 17):
    my_turtle.forward(n)
    my_turtle.left(120)
    n = n+ 10
n=10
my_turtle.left(120)
for i in range(0, 18):
    my_turtle.forward(n)
    my_turtle.left(120)
    n = n+ 10

n=10
my_turtle.left(120)
for i in range(0, 18):
    my_turtle.forward(n)
    my_turtle.left(120)
    n = n+ 10

        
turtle.done()