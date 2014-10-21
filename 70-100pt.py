##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

line1 = rectangle = drawpad.create_rectangle(400,400,300,300)
line1 = drawpad.create_line(340,250,400,300)
line1 = drawpad.create_line(340,250,300,300)
door = drawpad.create_rectangle(340,400,360,365)

# Insert your code here to draw the house!


root.mainloop()
