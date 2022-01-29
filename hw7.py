from turtle import*

def diamond_flower(size=50, n=7, angle=30 ) :
    down()
    for i in range(n) :
        for j in range(2) :
            forward(size)
            right(angle)
            forward(size)
            right(180-angle)
        right(360/n)
    up()

speed(0)
delay(0)
up()

flower_dict = { 'trigems':(3,70), 'five':(5,50), 'richnine':(9,50), 'thinnine':(9,30), 'needle':(30,10)}

def draw(name) :
    if name in flower_dict :
        goto(0,0)
        clear()
        (n,angle) = flower_dict[name]
        diamond_flower(100,n,angle)
    else :
        if name == 'all' :
            goto(-200,0)
            clear()
            for key in flower_dict :
                (n,angle) = flower_dict[key]
                diamond_flower(50,n,angle)
                forward(200)
        else :
            print(name,'not found')
        

