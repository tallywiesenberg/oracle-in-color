import turtle
from web3 import Web3


s = 256

msg = "GM"
hash = Web3.keccak(text=msg).hex()

print("hash:", hash)
print("length:",len(hash) )

color = "#" + hash[2:8].upper()


t = turtle.Turtle()
t.fillcolor(color)
t.begin_fill()

for _ in range(4):
    t.forward(s)
    t.right(90)

t.end_fill()

t.hideturtle()
t.ht()
ts = t.getscreen()

ts.getcanvas().postscript(file="square.ps")