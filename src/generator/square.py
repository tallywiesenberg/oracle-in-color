import cairo, sys, argparse, copy, math, random
import turtle
from web3 import Web3

#generate hash of message
s = 256

msg = "GM"
hash = Web3.keccak(text=msg).hex()

#create colors from hash
idx = 2
colors = []
while idx < len(hash)
colors = "#" + hash[2:8].upper()


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