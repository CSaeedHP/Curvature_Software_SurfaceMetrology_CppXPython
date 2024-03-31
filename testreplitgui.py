from tkinter import *
from tkinter import ttk

window = Tk()
c = 'c'
window.attributes('-fullscreen', True)
window.title("Very Epic Coke Machine")
ttk.Frame(window, padding=10)

coins = []
paidcoins = Label(window, text="Amount paid: " + str(sum(coins)) + c)
rem = Label(window, text="Amount due: " + str(50 - sum(coins)) + c)

def x():
  global coins
  global c
  coins.append(5)
  paidcoins.config(text="Amount paid: " + str(sum(coins)) + c)
  rem.config(text="Amount due: " + str(50 - sum(coins)) + c)
  if sum(coins) >= 50:
    paidcoins.config(text="All paid for!")
    if sum(coins) == 50:
      rem.config(text="No change!")
    elif sum(coins) > 50:
      rem.config(text="Change: " + str(sum(coins)-50) + c)
    nickel["state"] = DISABLED
    dime["state"] = DISABLED
    quarter["state"] = DISABLED

def y():
  global coins
  global c
  coins.append(10)
  paidcoins.config(text="Amount paid: " + str(sum(coins)) + c)
  rem.config(text="Amount due: " + str(50 - sum(coins)) + c)
  if sum(coins) >= 50:
    paidcoins

window.mainloop()