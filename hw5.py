from turtle import*
delay(0)

n=10
angle = 360/n

for k in range(10,100,10) :
    for i in range(n) :
        forward(k)
        right(angle)
        forward(k)
        right(180-angle)
        forward(k)
        right(angle)
        forward(k)
        right(180-angle)

        right(angle)
        
