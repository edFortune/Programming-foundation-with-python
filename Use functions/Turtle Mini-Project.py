import turtle

#This program write my initial name Edmael Fortune to EF

def draw_initial():
    #this is the screen object
    window = turtle.Screen()
    window.bgcolor("white")

    #The object Turtle that will draw lines
    pointer = turtle.Turtle()

    #The beginning of the initial E
    pointer.forward(100)
    pointer.right(180)
    pointer.forward(100)
    pointer.left(90)

    pointer.forward(100)
    pointer.left(90)
    pointer.forward(100)
    pointer.right(180)
    pointer.forward(100)

    pointer.left(90)
    pointer.forward(100)
    pointer.left(90)
    pointer.forward(100)
    #The end of the initial E

    pointer.forward(100)#The space between them

    #The beginning of the initial F
    pointer.left(90)
    pointer.forward(200)

    pointer.right(90)
    pointer.forward(100)
    pointer.right(180)
    pointer.forward(100)

    pointer.left(90)
    pointer.forward(100)
    pointer.left(90)
    pointer.forward(100)
    #The end of the initial F



    window.exitonclick()

draw_initial()
