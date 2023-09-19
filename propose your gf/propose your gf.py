import turtle as tur

# Set screen geometry
tur.setup(1000, 800)

tur.title("I Love You ABC")#replace with your gf name
tur.bgcolor("black")  # Set the background color to black

# Draw the text at the top left of the screen
tur.penup()
tur.goto(-250, 250)  # Set the position at the top left of the screen
tur.pendown()
tur.color("red")  # Set the text color to red
tur.write("Specially for you .....!!!!\n", align="left", font=("times new roman", 30, "italic", "bold"))

# Set initial position for drawing the rose
tur.penup()
tur.goto(0, 180)
tur.pendown()
tur.pencolor("blue")
# Flower base
tur.fillcolor("red")
tur.begin_fill()
tur.circle(10, 180)
tur.circle(25, 110)
tur.left(50)
tur.circle(60, 45)
tur.circle(20, 170)
tur.right(24)
tur.fd(30)
tur.left(10)
tur.circle(30, 110)
tur.fd(20)
tur.left(40)
tur.circle(90, 70)
tur.circle(30, 150)
tur.right(30)
tur.fd(15)
tur.circle(80, 90)
tur.left(15)
tur.fd(45)
tur.right(165)
tur.fd(20)
tur.left(155)
tur.circle(150, 80)
tur.left(50)
tur.circle(150, 90)
tur.end_fill()

# Petal 1
tur.left(150)
tur.circle(-90, 70)
tur.left(20)
tur.circle(75, 105)
tur.setheading(60)
tur.circle(80, 98)
tur.circle(-90, 40)

# Petal 2
tur.left(180)
tur.circle(90, 40)
tur.circle(-80, 98)
tur.setheading(-83)

# Leaves 1
tur.fd(30)
tur.left(90)
tur.fd(25)
tur.left(45)
tur.fillcolor("green")
tur.begin_fill()
tur.circle(-80, 90)
tur.right(90)
tur.circle(-80, 90)
tur.end_fill()
tur.right(135)
tur.fd(60)
tur.left(180)
tur.fd(85)
tur.left(90)
tur.fd(80)

# Leaves 2
tur.right(90)
tur.right(45)
tur.fillcolor("green")
tur.begin_fill()
tur.circle(80, 90)
tur.left(90)
tur.circle(80, 90)
tur.end_fill()
tur.left(135)
tur.fd(60)
tur.left(180)
tur.fd(60)
tur.right(90)
tur.circle(226, 60)

# Heart
tur.pensize(4)
tur.color("red")
tur.left(50)
tur.forward(200)
tur.circle(70, 200)
tur.right(140)
tur.circle(70, 200)
tur.forward(200)

# Write additional text
tur.penup()
tur.goto(-750, -350)  # Set the position for additional text
tur.pendown()
tur.color("red")  # Set the text color to red
tur.write(
    "From the moment our paths crossed,\n something extraordinary happened in my heart. \nYour smile became my sunshine,\n your laughter my favorite song.\n I've discovered a universe in your eyes,\n a sense of belonging in your presence.\n"
    "\n\nBut it's not just about how you make me feel; it's about us.\n Our conversations are a journey,\n your intelligence and passion inspire me,\n and your strength fuels my own."
    "\n\nI want you to know,\nit's not just a fleeting feeling.\n It's a profound love,\n a desire to stand by your side through life's highs and lows,\n to build a future together filled with\n love, laughter, and endless adventures.",
    align="left", font=("Times New Roman", 20, "italic"))

# Write additional text
tur.penup()
tur.goto(250, -400)  # Set the position for additional text
tur.pendown()
tur.color("red")  # Set the text color to red
tur.write(
    "Love is a masterpiece painted by the heart,"
    "\nwhere every stroke is a moment shared,"
    "\nand every color is an emotion felt,"
    "\ncreating a canvas of endless beauty 💖🎨.",
    align="left", font=("Times New Roman", 20, "italic"))

tur.done()
