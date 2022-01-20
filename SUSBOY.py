
from tkinter import *
from PIL import ImageTk, Image

root= Tk()
root.title("Working On Canvas Using Functions")
root.geometry("600x600")


color_label=Label(root, text="Enter a Color :")
color_label.place(relx=0.6,rely=0.95, anchor= CENTER)
color_label2=Label(root, text="Enter a width :")
color_label2.place(relx=0.2,rely=0.95, anchor= CENTER)
input_box = Entry(root)
input_box.insert(0,"black")
input_box.place(relx=0.8,rely=0.95, anchor= CENTER)
input_box2 = Entry(root)
input_box2.insert(0,5)
input_box2.place(relx=0.4,rely=0.95, anchor= CENTER)
color1=""
width=0

canvas=Canvas(root, width = 590, height=510, bg = "white", highlightbackground="lightgray")
direction = ""
oldx=50
oldy=50
newx=50
newy=50
def left_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    oldy=newy
    newx=newx-10
    direction="left"
    draw(direction,oldx,oldy,newx,newy)
def right_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    oldy=newy
    newx=newx+10
    direction="right"
    draw(direction,oldx,oldy,newx,newy)
def up_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    oldy=newy
    newy=newy-10
    direction="up"
    draw(direction,oldx,oldy,newx,newy)
def down_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    oldy=newy
    newy=newy+10
    direction="down"
    draw(direction,oldx,oldy,newx,newy)
def draw(direction,oldx,oldy,newx,newy):
    global color1
    global width
    color1=input_box.get()
    width=input_box2.get()
    if direction=="left":
        left_line = canvas.create_line(oldx,oldy,newx,newy,width=width,fill=color1)
    if direction=="right":
        right_line = canvas.create_line(oldx,oldy,newx,newy,width=width,fill=color1)
    if direction=="up":
        up_line = canvas.create_line(oldx,oldy,newx,newy,width=width,fill=color1)
    if direction=="down":
        down_line = canvas.create_line(oldx,oldy,newx,newy,width=width,fill=color1)

canvas.pack()
root.bind("<Left>",left_dir)
root.bind("<Right>",right_dir)
root.bind("<Up>",up_dir)
root.bind("<Down>",down_dir)
root.mainloop()

