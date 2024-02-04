from turtle import *


#we want to paint a house

#step 1:drow a square

width(7)

color("purple")
forward(200)
left(90)
forward(200)
left(90)        
forward(200)
left(90)
forward(200)
left(90)  
 #end squer    
#drowing  a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)           #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drow a window
color("blue")
penup()
goto(200,200)
pendown()
right(60)
forward(200)
left(90)
forward(55)
left(90)
forward(200)
left(90)
forward(55)
left(90)
forward(100)
left(90)
forward(55)
penup()
goto(200,200)
pendown()
left(10)
forward(25)
right(100)
forward(200)
exitonclick()
