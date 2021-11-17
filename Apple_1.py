#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
appleList = []
appleLetters = []

letters = ['A', 'S', 'D', 'F']

for i in range(5):
  appleList.append(trtl.Turtle())
  appleLetters.append(rand.choice(letters))

apple = trtl.Turtle()
appleLetter = 'A'

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(index):

  global appleLetter
  appleList[index].pu()
  appleList[index].shape(apple_image)
  wn.tracer(False)
  appleList[index].setx(rand.randint(-175,175))
  appleList[index].sety(rand.randint(-25,100))
  appleList[index].sety(appleList[index].ycor()-35)
  appleList[index].color("white")
  appleList[index].write(appleLetters[index], align="center",font=("Ariel", 40, "bold"))
  appleList[index].sety(appleList[index].ycor()+35)
  appleList[index].showturtle()
  wn.tracer(True)
  wn.update()

def drop_apple(index):
  appleList[index].pu()
  appleList[index].clear()
  appleList[index].sety(-150)
  appleList[index].hideturtle()
  draw_apple(i)

def typedA():
  for i in range(5):
    if appleLetters[i] == 'A':
      drop_apple(i)

def typedS():
  for i in range(5):
    if appleLetters[i] == 'S':
      drop_apple(i)

def typedD():
  for i in range(5):
    if appleLetters[i] == 'D':
      drop_apple(i)

def typedF():
  for i in range(5):
    if appleLetters[i] == 'F':
      drop_apple(i)

#-----function calls-----
for i in range(5):  
  draw_apple(i)
wn.onkeypress(typedA, 'a')
wn.onkeypress(typedS, 's')
wn.onkeypress(typedD, 'd')
wn.onkeypress(typedF, 'f')






wn.listen()

wn.mainloop()
